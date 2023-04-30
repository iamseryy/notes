from datetime import datetime

from scr.main.model.note import Note
from scr.main.services.note_service import Note_service
from scr.main.view.ui.user_interface import User_interface


class Edit_note_template:
    def output(self):
        self._ui.output('\nEdit note')

        while True:
            id = self._ui.user_input("\nEnter note ID or an empty string to cancel: ")
            if not id:
                self._ui.output("\nCancelled\n")
                return

            if not id.isdigit() or int(id) < 1:
                self._ui.output("Invalid! Try Again")
                continue

            note = self._note_service.find_by_id(int(id))

            if not note:
                self._ui.output("\nNo note found\n")
                self._ui.press_enter_to_continue()
                return
            else:
                self._ui.output(f'\nID: {note.id}  CREATE DATE: {note.create_date}\nHEAD: {note.header}\nNOTE: {note.body}')

            header = self._ui.user_input("\nEnter note header or an empty string to skip: ")
            if not header:
                header = note.header

            note_body = self._ui.user_input("\nEnter note or an empty string to skip: ")
            if not note_body:
                note_body = note.body

            if header == note.header and note_body == note.body:
                self._ui.output("\nCancelled\n")
                self._ui.press_enter_to_continue()
                return

            note.header = header
            note.body = note_body

            self._note_service.update(note)
            self._ui.output("\ndone")
            self._ui.press_enter_to_continue()
            return


    _ui = User_interface()
    _note_service = Note_service()