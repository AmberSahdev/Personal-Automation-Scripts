"""
A script that takes a Kindle's "My Clippings.txt" (organized ascendingly by time anything in that Kindle was clipped/highlighted/noted) \
and converts it into  \
a file per book with only that book's clippings in it without the metadata \
such that you can copy/paste the output .txt file into a word file/google doc, beautify, and then convert to PDF.
"""

# Step 1: Collect Clippings into a dictionary
bookHighlights = dict() # key(Book Name): val(List of Highlights/Notes)
with open("My Clippings.txt", "r") as clippings:
    stateNum = 0 # 0: "==========", 1: Book Name, 2: highlight/note location and time, 3: empty line, 4+: clippings' contents
    stateBook = "" # Name of the book in the current state
    stateTimeandPlace = "" # Currently unused
    stateType = "" # Either "Note" or "Highlight"

    for line in clippings:
        stateNum += 1
        if line == "==========\n":
            # reset state machine
            stateNum = 0
        else:
            if stateNum == 1:
                stateBook = line.strip()
                if stateBook not in bookHighlights.keys():
                    bookHighlights[stateBook] = []
            elif stateNum == 2:
                stateTimeandPlace = line
                stateType = line.strip().split()[2]
            elif stateNum == 3:
                continue
            else:
                if stateType == "Note":
                    bookHighlights[stateBook].append("Personal Note: (" + line.strip() + ")\n")
                elif stateType == "Highlight":
                    bookHighlights[stateBook].append(line)

# Step 2: Write each key-value pair into a .txt file
for bookName in bookHighlights.keys():
    print(bookName)
    with open(bookName+".txt", "w") as out:
        out.write(bookName + "\n")
        for line in bookHighlights[bookName]:
            out.write(line + "\n")
