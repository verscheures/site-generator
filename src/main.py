from textnode import TextNode, TextType


def main():
    textnode = TextNode("Hello, World!", TextType.NORMAL, "http://verscheure.dev")
    print(textnode)


if __name__ == "__main__":
    main()
