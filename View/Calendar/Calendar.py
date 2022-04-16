from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.core.window import Window
import calendar
import json

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '200')


with open("../RowJsonInfo/CalendarMonths.json", "r") as file:
    months = json.load(file)
YEAR = 2022
MONTH_AMOUNT = 12


class CalendarDaysLayout(GridLayout):
    def __init__(self, days, month_number, root_calendar):
        super(CalendarDaysLayout, self).__init__()
        self.month_number = month_number
        self.root_calendar = root_calendar
        self.cols = 7
        self.rows = 5
        self.padding = 10
        self.spacing = 10
        for day in range(days):
            self.add_widget(Button(text=str(day + 1),
                                   font_size=25,
                                   color=[1, 1, 0, 1],
                                   background_color=[1, .1, .4, 1]))

    def button_press(self, instance):
        sent_date = "{0}-{1}-{2}".format(str(YEAR),
                                         push_zero_to_date(str(self.month_number)),
                                         push_zero_to_date(instance.text))
        self.root_calendar.set_current_working_date(sent_date)
        self.root_calendar.apply_current_working_screen()


class CalendarScreen(Screen):
    def __init__(self, month_number, root_calendar):
        super(CalendarScreen, self).__init__()
        self.name = months[month_number]
        main_screen_layout = BoxLayout(orientation='vertical',
                                       spacing=20)
        kid_screen_layout = BoxLayout(orientation='horizontal',
                                      spacing=20,
                                      size_hint=[1, .5])
        kid_screen_layout.add_widget(Button(text="Previous",
                                            on_press=self.month_change_on_press,
                                            font_size=30,
                                            color=[1, 1, 0, 1],
                                            size_hint=[1, .5],
                                            pos_hint={'center_y': .5},
                                            background_color=[1, .1, .9, 1]))
        kid_screen_layout.add_widget(Label(text=self.name,
                                           font_size=45,
                                           color=[.5, .8, .5, 1]))
        kid_screen_layout.add_widget(Button(text="Next",
                                            on_press=self.month_change_on_press,
                                            font_size=30,
                                            color=[1, 1, 0, 1],
                                            size_hint=[1, .5],
                                            pos_hint={'center_y': .5},
                                            background_color=[1, .1, .9, 1]))
        main_screen_layout.add_widget(kid_screen_layout)
        main_screen_layout.add_widget((CalendarDaysLayout(calendar.monthrange(YEAR, month_number + 1)[1], month_number, root_calendar)))
        self.add_widget(main_screen_layout)

    def month_change_on_press(self, instance):
        if instance.text == "Previous":
            self.manager.current = self.manager.previous()
        elif instance.text == "Next":
            self.manager.current = self.manager.next()


class Calendar(ScreenManager):
    def __init__(self, manager):
        super(Calendar, self).__init__()
        self.current_working_date = None
        self.next_working_screen = None
        self.manager = manager
        Window.clearcolor = (.1, .1, .1, 1)
        for month in range(MONTH_AMOUNT):
            self.add_widget(CalendarScreen(month, self))

    def set_current_working_date(self, press_date):
        self.current_working_date = press_date

    def set_next_working_screen(self, working_screen):
        self.next_working_screen = working_screen

    def apply_current_working_screen(self):
        self.manager.current = self.next_working_screen


def push_zero_to_date(number: str):
    if len(number) == 1:
        return "0" + number
    else:
        return number


class LocalApp(App):
    def build(self):
        return Calendar()


if __name__ == "__main__":
    example = LocalApp()
    example.run()
