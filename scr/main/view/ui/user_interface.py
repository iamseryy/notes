class User_interface:
    def __init__(self):
        pass

    def output(self, message):
        print(message)

    def user_input(self, message):
        return input(message)

    def press_enter_to_continue(self):
        self.user_input("\nPress Enter to continue...")
