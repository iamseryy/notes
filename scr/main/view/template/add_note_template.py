from datetime import datetime

from scr.main.model.note import Note
from scr.main.services.note_service import Note_service
from scr.main.view.ui.user_interface import User_interface


class Add_note_template:
    def output(self):
        self._ui.output('\nAdd note')

        while True:
            header = self._ui.user_input("\nEnter note header or an empty string to cancel: ")
            if not header:
                self._ui.output("\nCancelled\n")
                return

            note_body = self._ui.user_input("\nEnter note or an empty string to cancel: ")
            if not note_body:
                self._ui.output("\nCancelled\n")
                return

            id = self._note_service.find_last_id()
            if id == 0:
                id = 1
            else:
                id += 1

            self._note_service.add(Note(id, header, note_body, datetime.now()))

            self._ui.press_enter_to_continue()
            return

    _ui = User_interface()
    _note_service = Note_service()