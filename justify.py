#!/usr/bin/python3
"""
Write a program in Python, that can accept a paragraph string and and page
width and return an array of left AND right justified strings.  NOTE: No words
should be broken, the beginning and end of the line should be characters).

You should provide instructions on how to execute your program and provide a
sample output.

Example:

Sample input:

Paragraph = "This is a sample text but a complicated problem to be solved, so
we are adding more text to see that it actually works."

Page Width = 20


Output should look like this:

Array [1] = "This  is  a   sample"
Array [2] = "text      but      a"
Array [3] = "complicated  problem"
Array [4] = "to be solved, so  we"
Array [5] = "are adding more text"
Array [6] = "to   see   that   it"
Array [7] = "actually      works.”
"""
import sys

def justify_text(text, width):
    """Justify text to width and return a list of strings."""
    wordlist = text.split()

    # Build a list of lines that will fit in justified format with room for
    # at least one space between each word.
    lines = []
    line = []
    length = 0
    for word in wordlist:
        wordlen = len(word)
        if length + wordlen <= width:
            line.append(word)
            length += wordlen
        else:
            lines.append(line)
            line = []
            line.append(word)
            length = wordlen

        # Allows at least one space between words
        if length < width:
            length += 1

    # Handles last line, and single word lines
    if line:
        lines.append(line)

    apply_spacing(lines, width)
    return lines


def apply_spacing(lines, width):
    """Space out each line to meet the width requirements."""
    for i, line in enumerate(lines):
        llen = sum([len(word) for word in line])

        if len(line)-1:
            joinspaces = ' ' * ((width - llen) // (len(line)-1))
            extraspace = ' ' * ((width - llen) % (len(line)-1))
        else:
            joinspaces = ''
            extraspace = ' ' * (width - llen)

        # line[0] += extraspace
        line[-1] = extraspace + line[-1]

        lines[i] = joinspaces.join(line)


def show_justified_text_as_array_lines(justified_text):
    """Show the justified with 'array number' headers."""
    for i, e in enumerate(justified_text):
        print(f'Array [{i+1}] = "{e}"')


def main():
    """Accept text string and page width and output array list of justified
       text."""
    if len(sys.argv) == 3:
        paragraph = sys.argv[1]
        page_width = int(sys.argv[2])
    else:
        paragraph = """This is a sample text but a complicated problem to be
        solved, so we are adding more text to see that it actually works."""
        page_width = 20

    justified_text = justify_text(paragraph, page_width)
    show_justified_text_as_array_lines(justified_text)


if __name__ == '__main__':
    main()
