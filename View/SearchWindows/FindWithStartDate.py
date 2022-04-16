from View.Calendar.Calendar import Calendar
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from Controller import TrainTableController


class FindWithStartDate(Screen):
    def __init__(self, controller, calendar):
        super(FindWithStartDate, self).__init__()
        self.name = "start date search"
        self.controller = controller
        self.calendar = calendar
        self.dialog_window = Label(text="Dialog window")
        self.date_output = Label(text="")
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(Button(text="Set start train date:", disabled=True))
        main_layout.add_widget(self.date_output)
        main_layout.add_widget(Button(text="Open calendar", on_press=self.press_calendar_open))
        main_layout.add_widget(Button(text="Search", on_press=self.press_search))
        main_layout.add_widget(self.dialog_window)
        self.add_widget(main_layout)

    def press_calendar_open(self, instance):
        self.calendar.set_next_working_screen(self.name)
        self.manager.current = "calendar screen"

    def press_search(self, instance):
        if self.date_output.text == "":
            self.dialog_window.text = "Error"
            return
        else:
            self.dialog_window.text = ""
            self.text_input.text = ""
            self.manager.current = "search result"



