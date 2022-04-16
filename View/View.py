from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from datetime import datetime


class MyTableLabel(Label):
    def __init__(self):
        super(MyTableLabel, self).__init__()


class ViewTableNote(BoxLayout):
    def __init__(self,
                 note_number,
                 start_station,
                 end_station,
                 start_datetime,
                 end_datetime,
                 path_time,
                 amount_of_neighbours
                 ):
        super(ViewTableNote, self).__init__()
        self.orientation = 'horizontal'
        self.spacing = 5
        self.size_hint = [1, 1/amount_of_neighbours]
        self.add_widget(Label(text=str(note_number),
                              size_hint=[0.1, 1]))
        self.add_widget(Label(text=str(start_station),
                              size_hint=[0.2, 1]))
        self.add_widget(Label(text=str(end_station),
                              size_hint=[0.2, 1]))
        self.add_widget(Label(text=str(start_datetime),
                              size_hint=[0.2, 1]))
        self.add_widget(Label(text=str(end_datetime),
                              size_hint=[0.2, 1]))
        self.add_widget(Label(text=str(path_time),
                              size_hint=[0.1, 1]))


class ViewTableScreen(Screen):
    def __init__(self, amount_of_neighbours):
        super(ViewTableScreen, self).__init__()
        self.amount_of_neighbours = amount_of_neighbours
        main_layout = BoxLayout(orientation='vertical')


class LocalApp(App):
    def build(self):
        datetime1 = datetime.now()
        #return ViewTableNote(1, "Malinauka", "Malinauka", datetime1, datetime1, datetime1, 7)
        return MyTableLabel()


if __name__ == "__main__":
    Example = LocalApp()
    Example.run()
