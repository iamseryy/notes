from scr.main.services.note_service import Note_service
from scr.main.view.ui.user_interface import User_interface


class Selected_note_by_id_template:

    def output(self):
        self._ui.output('\nView selected note by ID')
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
            else:
                self._ui.output(f'ID: {note.id}  CREATE DATE: {note.create_date}\nHEAD: {note.header}\nNOTE: {note.body}')

            self._ui.press_enter_to_continue()
            return

    _ui = User_interface()
    _note_service = Note_service()