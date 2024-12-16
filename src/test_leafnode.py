import unittest

from leafnode import LeafNode


class TestLeaf(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        assert node.to_html() == "<p>This is a paragraph of text.</p>"

    def test_to_html_no_tag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        assert node.to_html() == "This is a paragraph of text."

    def test_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
