from scr.main.view.ui.user_interface import User_interface


class Exit_template:
    def output(self):
        self._ui.output('\nApplication closed')

    _ui = User_interface()