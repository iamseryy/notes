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

            if not id.isdigit() or int(id) < 1:
                self._ui.output("Invalid! Try Again")
                continue

            note = self._note_service.find_by_id(int(id))
            if not note:
                self._ui.output("\nNo note found\n")
            else:
                self._ui.output(
                    f'ID: {note.id}  CREATE DATE: {note.create_date}\nHEAD: {note.header}\nNOTE: {note.body}')

            self._ui.press_enter_to_continue()
            return

    _ui = User_interface()
    _note_service = Note_service()


    _ui = User_interface()