"""
Feature Lists::
Inserting
Deleting
Selecting
Cut
Copy
Paste
Save
Close

TODO: Do some error handling here
"""

from typing import List


class Character:
    def __init__(self, character, bold=False, italic=False, underlined=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underlined = underlined

    def __str__(self):
        bold = "*" if self.bold else ""
        italic = "/" if self.italic else ""
        underlined = "_" if self.underlined else ""
        return bold + italic + underlined + self.character


class Cursor:
    def __init__(self, document: "Document"):
        self.document = document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        while (
            self.position > 0
            and self.document.characters[self.position - 1].character != "\n"
        ):
            # As long as the previous character isn't a new line, go backwards
            self.position -= 1

    def end(self):
        while (
            self.position < len(self.document.characters) - 1
            and self.document.characters[self.position + 1].character != "\n"
        ):
            self.position += 1


class Document:
    def __init__(self):
        self.characters: List[Character] = []
        self.cursor = Cursor(self)
        self.filename = ""

    def insert(self, character: Character):
        if not isinstance(character, Character):
            character = Character(character)
        self.characters.insert(
            self.cursor.position, character
        )  # Add a character at the cursof position
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        with open(self.filename, "w") as f:
            f.write("".join([str(c) for c in self.characters]))

    @property
    def string(self):
        return "".join([str(c) for c in self.characters])


def test_document_viewer():
    doc = Document()
    doc.filename = "viewer_test.txt"

    doc.insert("H")
    doc.insert("e")
    doc.insert("l")
    doc.insert("l")
    doc.insert("o")
    doc.insert(" ")
    doc.insert("W")
    doc.insert("o")
    doc.insert("r")
    doc.insert("l")
    doc.insert("d")

    doc.cursor.home()
    doc.insert(">")
    doc.cursor.end()
    doc.insert("<")

    print("Document content:", doc.string)

    doc.save()
    print("Document saved as:", doc.filename)


test_document_viewer()
