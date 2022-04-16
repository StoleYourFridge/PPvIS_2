from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.uix.button import Button
from ViewTrainNote import ViewTrainNote
from ViewTrainTabelScreen import ViewTrainTableScreen


class ViewTrainScreenManager(ScreenManager):
    def __init__(self, amount_of_screen_elements):
        super(ViewTrainScreenManager, self).__init__()
        self.amount_of_screen_elements = amount_of_screen_elements
        self.current_screen = None
        self.create_new_screen()

    def generate_screen_name(self):
        return str(len(self.screens) + 1)

    def create_new_screen(self):
        self.current_screen = ViewTrainTableScreen(self.amount_of_screen_elements,
                                                   self.generate_screen_name())
        self.add_widget(self.current_screen)

    def create_new_table_note(self, new_note):
        if self.current_screen.is_new_screen_necessary():
            self.create_new_screen()
        self.current_screen.add_widget(new_note)
        self.current_screen.increase_amount_of_elements()


class LocalApp(App):
    def build(self):
        root = ViewTrainTableScreen(5, "name")
        for i in range(2):
            root.add_widget(ViewTrainNote("1", "2", "3", "4", "5", "6", 5))
        return root


if __name__ == "__main__":
    local_app = LocalApp()
    local_app.run()
