import csv
import datetime

from scr.main.config.properties import FILE_NOTES
from scr.main.model.note import Note


class Notes:
    def find_all(self):
        return self._notes

    def add(self, note):
        self._notes.append(note)
        self._write_to_file(self._notes)

    def update(self, note):
        index = self._find_index_by_id(self._notes, note.id)
        self._notes[index] = note
        self._write_to_file(self._notes)

    def remove(self, note):
        self._notes.remove(note)
        self._write_to_file(self._notes)

    def _write_to_file(self, notes):
        data = [[item.id, item.header, item.body, item.create_date.strftime("%Y-%m-%d %H:%M:%S")] for item in notes]
        with open(FILE_NOTES, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(data)

    def note_binary_search_by_id(self, notes, id):
        found_index = self._find_index_by_id(notes, id)
        if not found_index:
            return
        else:
            return notes[found_index]

    def _find_index_by_id(self, notes, id):
        mid = len(notes) // 2
        low = 0
        high = len(notes) - 1

        while notes[mid].id != id and low <= high:
            if id > notes[mid].id:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        if low > high:
            return
        else:
            return mid

    @staticmethod
    def _init_list():
        with open(FILE_NOTES, encoding='utf-8') as file:
            data = csv.reader(file, delimiter=";")
            notes = []
            for row in data:
                note = Note(int(row[0]), row[1], row[2], datetime.datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S"))
                notes.append(note)
        return notes

    _notes = _init_list()
