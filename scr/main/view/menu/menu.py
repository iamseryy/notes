from scr.main.view.ui.user_interface import User_interface


class Menu:
    def __init__(self):
        pass

    def processing(self, menu_header, menu_item_list):
        while True:
            self._ui.output(f'{menu_header}\n')
            self._ui.output('\n'.join([menu_item.description for menu_item in menu_item_list]))

            item_optional = self._ui.user_input("\nChoose your option: ")

            if not item_optional or not item_optional.isdigit() \
                    or int(item_optional) > len(menu_item_list) or int(item_optional) < 1:
                self._ui.output("Invalid! Try Again")
                self._ui.press_enter_to_continue()
                continue

            menu_item = menu_item_list[int(item_optional) - 1]
            menu_item.exec_func()

            if int(item_optional) == len(menu_item_list):
                return

    _ui = User_interface()
