from scr.main.services.note_service import Note_service
from scr.main.view.ui.user_interface import User_interface


class Note_list_template:

    def output(self):
        self._ui.output('\nNote list')
        notes = self._note_service.find_all()
        if notes:
            self._ui.output('\n'.join([f'ID: {note.id}; HEAD: {note.header}; CREATE DATE: {note.create_date.strftime("%Y-%m-%d %H:%M:%S")}' for note in notes]))
        else:
            self._ui.output("\nNo note found\n")

        self._ui.press_enter_to_continue()

    _ui = User_interface()
    _note_service = Note_service()
