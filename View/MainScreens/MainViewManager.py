from kivy.uix.screenmanager import ScreenManager
from Controller.TrainTableController import TrainTableController
from View.MainScreens.MainScreens import StartScreen, NewNoteAdditionScreen, SearchScreen, DeleteScreen
from View.MainScreens.MainScreens import AllNotesOutputScreen, CalendarScreen, FileManagementScreen
from View.Calendar.Calendar import Calendar
from kivymd.app import MDApp


class MainViewManager(ScreenManager):
    def __init__(self):
        super(MainViewManager, self).__init__()
        self.controller = TrainTableController()
        self.calendar = Calendar(self)
        self.add_widget(StartScreen())
        self.add_widget(NewNoteAdditionScreen())
        self.add_widget(DeleteScreen())
        self.add_widget(AllNotesOutputScreen())
        self.add_widget(FileManagementScreen())
        search_screen = SearchScreen()
        search_screen.addition()
        calendar_screen = CalendarScreen()
        calendar_screen.main_layout.add_widget(self.calendar)
        self.add_widget(search_screen)
        self.add_widget(calendar_screen)


class MainScreensApp(MDApp):
    def build(self):
        return MainViewManager()
