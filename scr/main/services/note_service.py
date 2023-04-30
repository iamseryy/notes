from scr.main.repository.notes import Notes


class Note_service:
    def __int__(self):
        pass

    def find_all(self):
        return self._notes.find_all()

    def find_by_id(self, id):
        return self._notes.note_binary_search_by_id(self._notes.find_all(), id)

    def find_last_id(self):
        notes = self._notes.find_all()
        if notes:
            return max(self._notes.find_all(), key=lambda note: note.id).id
        else:
            return 0

    def add(self, note):
        self._notes.add(note)

    def update(self, note):
        self._notes.update(note)

    def remove(self, note):
        self._notes.remove(note)

    def find_by_created_date_range(self, date_from, date_to):
        return list(filter(lambda note: date_from <= note.create_date <= date_to, self._notes.find_all()))

    _notes = Notes()
