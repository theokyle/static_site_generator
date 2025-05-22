import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_no_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_bad_data(self):
        node = HTMLNode(props = [5, 6])
        with self.assertRaises(TypeError):    
            node.props_to_html()
    

        

if __name__ == "__main__":
    unittest.main()