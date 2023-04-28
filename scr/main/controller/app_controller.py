from scr.main.model.note import Note
from scr.main.repository.notes import Notes
from scr.main.services.note_service import Note_service


def start():
    service = Note_service()
    note = service.find_by_id(0)
