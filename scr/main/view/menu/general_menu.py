from scr.main.view.menu.menu import Menu
from typing import Final
from scr.main.view.menu.menu_item import Menu_item
from scr.main.view.template.add_note_template import Add_note_template
from scr.main.view.template.exit_template import Exit_template
from scr.main.view.template.note_list_template import Note_list_template
from scr.main.view.template.selected_note_by_id_template import Selected_note_by_id_template

HEADER: Final = '\nNotes'
GENERAL_MENU_ITEMS: Final = [Menu_item("1. Add note list", lambda: Add_note_template().output()),
                             Menu_item("2. View note list", lambda: Note_list_template().output()),
                             Menu_item("3. View selected note by ID", lambda: Selected_note_by_id_template().output()),
                             Menu_item("4. Exit", lambda: Exit_template().output())]


class General_menu(Menu):
    def __init__(self):
        pass

    def processing(self):
        super().processing(HEADER, GENERAL_MENU_ITEMS)
