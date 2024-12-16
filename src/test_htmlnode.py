import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "A",
            None,
            None,
            {
                "href": "https://www.google.com",
                "tarrget": "_blank",
            },
        )
        self.assertEqual(
            node.props_to_html(),
            ' "href"="https://www.google.com" "tarrget"="_blank"',
        )

    def test_props_to_html_none(self):
        node = HTMLNode("A")
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(
            "A",
            None,
            None,
            {
                "href": "https://www.google.com",
                "tarrget": "_blank",
            },
        )
        self.assertEqual(
            str(node),
            "HTMLNode(A, None, None, {'href': 'https://www.google.com', 'tarrget': '_blank'})",
        )
