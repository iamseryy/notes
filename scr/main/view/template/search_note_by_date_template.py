from datetime import datetime

from scr.main.services.note_service import Note_service
from scr.main.view.ui.user_interface import User_interface


class Search_note_by_date_template:
    def output(self):
        self._ui.output('\nSearch note by date')

        while True:
            date_from_str = self._ui.user_input("\nEnter date from (YYYY-MM-DD) or an empty string to cancel: ")
            if not date_from_str:
                self._ui.output("\nCancelled\n")
                return

            if not self._date_validate(date_from_str):
                self._ui.output("Incorrect data format, should be YYYY-MM-DD! Try Again")
                continue

            date_to_str = self._ui.user_input("\nEnter date to (YYYY-MM-DD) or an empty string to cancel: ")
            if not date_to_str:
                self._ui.output("\nCancelled\n")
                return

            if not self._date_validate(date_to_str):
                self._ui.output("Incorrect data format, should be YYYY-MM-DD! Try Again")
                continue

            dt = datetime.strptime(date_from_str, '%Y-%m-%d')
            date_from = dt.replace(hour=0, minute=0, second=0)
            dt = datetime.strptime(date_to_str, '%Y-%m-%d')
            date_to = dt.replace(hour=23, minute=59, second=59)

            if date_from > date_to:
                self._ui.output("\nDate from must be greater than date to! Try Again")
                continue

            found_notes = self._note_service.find_by_created_date_range(date_from, date_to)
            if not found_notes:
                self._ui.output("\nNo note found\n")
                self._ui.press_enter_to_continue()
                return

            self._ui.output('\n'.join(
                [
                    f'\nID: {note.id}  CREATE DATE: {note.create_date.strftime("%Y-%m-%d %H:%M:%S")}\nHEAD: {note.header}\nNOTE: {note.body}'
                    for note in found_notes]))

            self._ui.press_enter_to_continue()
            return

    def _date_validate(self, date_text):
        try:
            if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
                raise ValueError
            return True
        except ValueError:
            return False

    _ui = User_interface()
    _note_service = Note_service()
