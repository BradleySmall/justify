"""
Write a program in Python, that can accept a paragraph string and and page
width and return an array of left AND right justified strings.  NOTE: No words
should be broken, the beginning and end of the line should be characters).

You should provide instructions on how to execute your program and provide a
sample output.

Example:

Sample input:

Paragraph = "This is a sample text but a complicated problem to be solved, so
we are adding more text to see that it actually works." Page Width = 20


Output should look like this:

Array [1] = "This  is  a   sample"
Array [2] = "text      but      a"
Array [3] = "complicated  problem"
Array [4] = "to be solved, so  we"
Array [5] = "are adding more text"
Array [6] = "to   see   that   it"
Array [7] = "actually      works.”
"""


def main():
    paragraph = """This is a sample text but a complicated problem to be
    solved, so we are adding more text to see that it actually works."""
    page_width = 20

    wordlist = paragraph.split()

    lines = []
    line = []
    length = 0
    for word in wordlist:
        wordlen = len(word)
        if length + wordlen <= page_width:
            line.append(word)
            length += wordlen
        else:
            lines.append(line)
            line = []
            line.append(word)
            length = wordlen

        if length < page_width:
            length += 1
    if line:
        lines.append(line)

    report = {}
    for num, line in enumerate(lines):
        llen = 0
        for word in line:
            llen += len(word)

        joinspaces = ''
        extraspace = ''
        if len(line)-1:
            joinspaces = ' ' * ((page_width - llen) // (len(line)-1))
            extraspace = ' ' * ((page_width - llen) % (len(line)-1))
        else:
            extraspace = ' ' * (page_width - llen)

        # line[0] += extraspace
        line[-1] = extraspace + line[-1]

        arrstr = "Array [%s]" % str(num+1)
        report[arrstr] = joinspaces.join(line)
        # print('Array [',num+1,'] = "', joinspaces.join(line), '"', sep='')

    for key, val in report.items():
        print(key, ' = "', val, '"', sep='')


main()
