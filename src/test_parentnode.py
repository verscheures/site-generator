import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParent(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        assert (
            node.to_html()
            == "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", []).to_html()

    def test_nested_parrents(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "b",
                    [
                        LeafNode(None, "Bold text"),
                        LeafNode(None, "Bold text"),
                    ],
                ),
                LeafNode(None, "Normal text"),
            ],
        )
        assert node.to_html() == "<p><b>Bold textBold text</b>Normal text</p>"
