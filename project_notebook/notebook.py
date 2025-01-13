import datetime
from typing import List
from utils import enforce_types

last_id = 0


class Note:
    """Represent a note in a notebook. Match against a string in searches and store tags for each note"""

    def __init__(self, memo, tags=""):
        """Initialize a note with memo and optional space-separated tags. Automatically set the note's creation date and a unique id"""
        self.memo: str = memo
        self.tags: str = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id: int = last_id

    def match(self, filter):
        """Determine if this note matches the filter text. Return true if it matches, false otherwise"""
        return filter in self.memo or filter in self.tags

    def __str__(self):
        return self.memo

    def __repr__(self):
        return f"{self.id} - {self.memo}"


class Notebook:
    """Represent a collection of notes that can be tagged, modified, and searched."""

    def __init__(self):
        """Initialize a notebook with an empty list"""
        self.notes = []

    def new_note(self, memo, tags=""):
        """Create a new note and add it to the list"""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id: int) -> Note:
        """Locate the note with the given id."""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id: int, memo: str) -> bool:
        """Find the note witht hei given id and change its memo to the given value"""

        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True

        return False

    def modify_tags(self, note_id: int, tags: str) -> bool:
        """Find the note with the given id and change its tags to the given value"""
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True

        return False

    def search(self, filter) -> List[Note]:
        """Find all notes that match the given filter"""
        return [note for note in self.notes if note.match(filter)]


if __name__ == "__main__":
    n = Notebook()
    n.new_note("Hello World")
    n.new_note("Hello Again")
    n.modify_tags(1, "Hii")
    print(n.notes)
    print(n.notes[0].tags)
