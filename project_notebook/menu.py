import sys
from notebook import Note, Notebook
from typing import List


class Menu:
    """Display a menu and respond to the choices when run"""

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
        }

    def display_menu(self):
        """Display"""
        print(
            "Notebook Menu\n\n1. Show all Notes\n2. Search Notes\n3. Add Note\n4. Modify Note\n5. Quit"
        )

    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)  # Safety if unusual input is given
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes: List[Note] = None):
        """Show notes. If not provided with specific notes, show all"""
        if not notes:
            notes: List[Note] = self.notebook.notes

        for note in notes:
            print("{0}: {1}\{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self, memo=None, tags=None):
        id = input("Enter the note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    menu = Menu()
    menu.notebook.new_note("Hello", "T2")
    menu.run()
