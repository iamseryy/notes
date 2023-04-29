from scr.main.model.note import Note
from scr.main.repository.notes import Notes
from scr.main.services.note_service import Note_service


def start():
    service = Note_service()
    notes1 = service.find_all()

    service.remove(service.find_by_id(4))
    new_note = Note(3, "test3", "body test3", "2023-04-30")
    service.add(new_note)

