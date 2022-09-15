#!/usr/bin/python3
"""
    First argument is the name of the Markdown file
    Second argument is the output file name
"""
if __name__ == "__main__":
    import sys
    from os import path


    md = {"#": "h1", "##": "h2", "###": "h3", "####": "h4", "#####": "h5", "######": "h6", "-": "ul", "*": "ol"}

    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not path.exists(sys.argv[1]) or not str(sys.argv[1]).endswith(".md"):
        sys.stderr.write("Missing " + sys.argv[1] + '\n')
        exit(1)
