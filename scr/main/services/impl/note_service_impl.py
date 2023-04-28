from scr.main.repository.notes import Notes
from scr.main.services.note_service import Note_service


class Note_service_impl(Note_service):
    def find_by_id(self, id):
        return [note for note in Note_service_impl._notes if note[0] == id]

    _notes = Notes()
