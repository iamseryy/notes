from scr.main.repository.notes import Notes


class Note_service:
    def __int__(self):
        pass

    def find_all(self):
        return self._notes.find_all()

    def find_by_id(self, id):
        for note in self._notes.find_all():
            if note.id == id:
                return note

    def find_last_id(self):
        return max(self._notes.find_all(), key=lambda note: note.id).id

    def add(self, note):
        self._notes.add(note)

    def remove(self, note):
        self._notes.remove(note)

    _notes = Notes()
