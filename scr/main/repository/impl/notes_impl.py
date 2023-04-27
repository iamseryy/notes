import csv

from scr.main.config.properties import FILE_NOTES
from scr.main.repository.notes import Notes


class Notes_impl(Notes):

    def find_by_id(self, id):
        return [note for note in Notes_impl._notes if note[0] == id]

    def _init_dictionary(self):
        with open(FILE_NOTES, "r", newline="") as file:
            reader = csv.reader(file)
        return reader

    _notes = _init_dictionary()
