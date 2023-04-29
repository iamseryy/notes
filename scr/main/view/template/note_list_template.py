from scr.main.services.note_service import Note_service
from scr.main.view.ui.user_interface import User_interface


class Note_list_template:

    def output(self):
        self._ui.output('\nNote list')
        self._ui.output('\n'.join([ f'ID: {note.id}; HEAD: {note.header}' for note in self._note_service.find_all()]))
        self._ui.press_enter_to_continue()

    _ui = User_interface()
    _note_service = Note_service()
