from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class ViewTrainNote(BoxLayout):
    def __init__(self,
                 train_number,
                 start_station,
                 end_station,
                 start_datetime,
                 end_datetime,
                 path_time,
                 amount_of_neighbours):
        super(ViewTrainNote, self).__init__()
        self.orientation = 'horizontal'
        self.spacing = 2
        self.size_hint = [1, 1/amount_of_neighbours]
        self.add_widget(Button(disabled=True,
                               text=train_number,
                               size_hint=[.1, 1]))
        self.add_widget(Button(disabled=True,
                               text=start_station,
                               size_hint=[.2, 1]))
        self.add_widget(Button(disabled=True,
                               text=end_station,
                               size_hint=[.2, 1]))
        self.add_widget(Button(disabled=True,
                               text=start_datetime,
                               size_hint=[.2, 1]))
        self.add_widget(Button(disabled=True,
                               text=end_datetime,
                               size_hint=[.2, 1]))
        self.add_widget(Button(disabled=True,
                               text=path_time,
                               size_hint=[.1, 1]))
