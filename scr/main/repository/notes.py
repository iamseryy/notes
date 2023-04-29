import csv

from scr.main.config.properties import FILE_NOTES
from scr.main.model.note import Note


class Notes:
    def __init__(self):
        pass

    def find_all(self):
        return self._notes

    def add(self, note):
        self._notes.append(note)
        self._notes.sort(key=lambda item: item.id)
        data = [[item.id, item.header, item.body, item.create_date] for item in self._notes]
        with open(FILE_NOTES, 'w', newline='') as file:
            writer = csv.writer(file, delimiter="|")
            writer.writerows(data)

    def remove(self, note):
        self._notes.remove(note)

    @staticmethod
    def _init_list():
        with open(FILE_NOTES, encoding='utf-8') as file:
            data = csv.reader(file, delimiter="|")
            notes = []
            for row in data:
                note = Note(int(row[0]), row[1], row[2], row[3])
                notes.append(note)
        return notes

    _notes = _init_list()
