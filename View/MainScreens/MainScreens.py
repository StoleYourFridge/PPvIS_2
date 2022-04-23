from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class StartScreen(Screen):
    def on_all_notes_output_button_press(self):
        self.manager.current = "AllNotesOutputScreen"

    def on_new_note_addition_button_press(self):
        self.manager.current = "NewNoteAdditionScreen"

    def on_search_button_press(self):
        self.manager.current = "SearchScreen"

    def on_delete_button_press(self):
        self.manager.current = "DeleteScreen"


class NewNoteAdditionScreen(Screen):
    def on_calendar_open_button_press(self):
        self.manager.calendar.set_next_working_screen(self.name)
        self.manager.current = "CalendarScreen"

    def on_apply_start_calendar_info_button_press(self):
        self.ids.start_date.text = self.manager.calendar.current_working_date

    def on_apply_end_calendar_info_button_press(self):
        self.ids.end_date.text = self.manager.calendar.current_working_date

    def on_back_button_press(self):
        self.manager.current = "StartScreen"

    def clear_widget_info(self):
        self.ids.dialog.text = "Dialog window"
        self.ids.station_grid.ids.start.text = ""
        self.ids.station_grid.ids.end.text = ""
        self.ids.start_date.text = ""
        self.ids.time_grid.ids.start.text = ""
        self.ids.end_date.text = ""
        self.ids.time_grid.ids.end.text = ""

    def on_apply_entered_info_button_press(self):
        if not self.manager.controller.add_new_note_validated(self.ids.station_grid.ids.start.text,
                                                              self.ids.station_grid.ids.end.text,
                                                              self.ids.start_date.text,
                                                              self.ids.time_grid.ids.start.text,
                                                              self.ids.end_date.text,
                                                              self.ids.time_grid.ids.end.text):
            self.ids.dialog.text = "Error"
            return
        else:
            self.clear_widget_info()
        return


class SearchDeleteTemplateScreenLayout(BoxLayout):
    parent_screen = ObjectProperty()


class SearchDeleteTemplateScreen(Screen):
    action_name = ""
    first_group_data = ""
    second_group_data = ""

    def on_calendar_open_button_press(self):
        self.manager.calendar.set_next_working_screen(self.name)
        self.manager.current = "CalendarScreen"

    def on_apply_calendar_info_button_press(self):
        self.ids.date_input.text = self.manager.calendar.current_working_date

    def on_back_button_press(self):
        self.clear_widget_info()
        self.manager.current = "StartScreen"

    def on_first_group_active(self, value, text):
        if value:
            self.first_group_data = text

    def on_second_group_active(self, value, text):
        if value:
            self.second_group_data = text

    def first_group_active_validation(self):
        if self.first_group_data == "":
            return False
        return True

    def second_group_active_validation(self):
        if self.second_group_data == "":
            return False
        return True

    def clear_widget_info(self):
        self.ids.train_number_input.text = ""
        self.ids.days_input.text = ""
        self.ids.hours_input.text = ""
        self.ids.minutes_input.text = ""
        self.ids.seconds_input.text = ""
        self.ids.station_input.text = ""
        self.ids.low_time_input.text = ""
        self.ids.top_time_input.text = ""
        self.ids.date_input.text = ""
        self.ids.dialog.text = "Dialog window"

    def number_search_sender(self):
        if not self.manager.controller.find_with_train_number_validated(self.ids.train_number_input.text):
            self.ids.dialog.text = "Error"
            return
        else:
            self.clear_widget_info()
            return

    def path_time_search_sender(self):
        if not self.manager.controller.find_with_path_time_validated(self.ids.days_input.text,
                                                                     self.ids.hours_input.text,
                                                                     self.ids.minutes_input.text,
                                                                     self.ids.seconds_input.text):
            self.ids.dialog.text = "Error"
            return
        else:
            self.clear_widget_info()
            return

    def station_search_sender(self):
        if self.first_group_data == "Start":
            if not self.manager.controller.find_with_start_station_validated(self.ids.station_input.text):
                self.ids.dialog.text = "Error"
                return
            else:
                self.clear_widget_info()
                return
        elif self.first_group_data == "End":
            if not self.manager.controller.find_with_end_station_validated(self.ids.station_input.text):
                self.ids.dialog.text = "Error"
                return
            else:
                self.clear_widget_info()
                return

    def time_range_search_sender(self):
        if self.first_group_data == "Start":
            if not self.manager.controller.find_in_start_time_range_validated(self.ids.low_time_input.text,
                                                                              self.ids.top_time_input.text):
                self.ids.dialog.text = "Error"
                return
            else:
                self.clear_widget_info()
                return
        elif self.first_group_data == "End":
            if not self.manager.controller.find_in_end_time_range_validated(self.ids.low_time_input.text,
                                                                            self.ids.top_time_input.text):
                self.ids.dialog.text = "Error"
                return
            else:
                self.clear_widget_info()
                return

    def date_search_sender(self):
        if self.first_group_data == "Start":
            if not self.manager.controller.find_with_start_date_validated(self.ids.date_input.text):
                self.ids.dialog.text = "Error"
                return
            else:
                self.clear_widget_info()
                return
        elif self.first_group_data == "End":
            if not self.manager.controller.find_with_end_date_validated(self.ids.date_input.text):
                self.ids.dialog.text = "Error"
                return
            else:
                self.clear_widget_info()
                return

    def on_action_button_press(self):
        if not self.second_group_active_validation():
            self.ids.dialog.text = "Error"
            return
        if self.second_group_data == "Number":
            self.number_search_sender()
            self.action()
            return
        elif self.second_group_data == "Path time":
            self.path_time_search_sender()
            self.action()
            return

        if not self.first_group_active_validation():
            self.ids.dialog.text = "Error"
            return
        if self.second_group_data == "Station":
            self.station_search_sender()
            self.action()
            return
        elif self.second_group_data == "Time range":
            self.time_range_search_sender()
            self.action()
            return
        elif self.second_group_data == "Date":
            self.date_search_sender()
            self.action()
            return

    def action(self):
        pass


class DeleteScreen(SearchDeleteTemplateScreen):
    name = "DeleteScreen"
    action_name = "Delete"

    def action(self):
        if self.ids.dialog.text == "Error":
            return
        delete_amount = len(self.manager.controller.corrected_search_version)
        self.manager.controller.delete_notes_with_buffer()
        self.ids.dialog.text = "Notes deleted : " + str(delete_amount)
        return


class SearchScreen(SearchDeleteTemplateScreen):
    name = "SearchScreen"
    action_name = "Search"

    def addition(self):
        self.data_table = MDDataTable(size_hint=[1, 1],
                                      use_pagination=True,
                                      column_data=[
                                          ("No.", dp(30)),
                                          ("Start Station", dp(70)),
                                          ("End Station", dp(70)),
                                          ("Start Datetime", dp(50)),
                                          ("End Datetime", dp(50)),
                                          ("Path Time", dp(50)),
                                      ])
        self.ids.main.add_widget(self.data_table)

    def add_row(self, train_number):
        addition_tuple = self.manager.controller.model.get_train_note_info_with_number(train_number)
        self.data_table.row_data.append(addition_tuple)

    def remove_row(self, train_number):
        for index in range(len(self.data_table.row_data)):
            if self.data_table.row_data[index][0] == str(train_number):
                self.data_table.row_data.pop(index)
                break

    def action(self):
        if self.ids.dialog.text == "Error":
            return
        difference = self.manager.controller.get_search_screen_difference()
        addition_set = difference["addition"]
        delete_set = difference["delete"]
        for number in addition_set:
            self.add_row(number)
        for number in delete_set:
            self.remove_row(number)


class AllNotesOutputScreen(Screen):
    def __init__(self):
        super(AllNotesOutputScreen, self).__init__()
        self.name = "AllNotesOutputScreen"
        main_layout = BoxLayout(orientation='vertical')
        self.data_table = MDDataTable(size_hint=[1, 1],
                                      use_pagination=True,
                                      column_data=[
                                          ("No.", dp(30)),
                                          ("Start Station", dp(70)),
                                          ("End Station", dp(70)),
                                          ("Start Datetime", dp(50)),
                                          ("End Datetime", dp(50)),
                                          ("Path Time", dp(50)),
                                      ])
        main_layout.add_widget(self.data_table)
        main_layout.add_widget(Button(text="Home",
                                      on_press=self.on_back_button_press,
                                      size_hint=(1, .1)))
        main_layout.add_widget(Button(text="Refresh table data",
                                      on_press=self.refresh_table_data,
                                      size_hint=(1, .1)))
        self.add_widget(main_layout)

    def on_back_button_press(self, instance):
        self.manager.current = "StartScreen"

    def add_row(self, train_number):
        addition_tuple = self.manager.controller.model.get_train_note_info_with_number(train_number)
        self.data_table.row_data.append(addition_tuple)

    def remove_row(self, train_number):
        for index in range(len(self.data_table.row_data)):
            if self.data_table.row_data[index][0] == str(train_number):
                self.data_table.row_data.pop(index)
                break

    def refresh_table_data(self, instance):
        difference = self.manager.controller.get_main_screen_difference()
        addition_set = difference["addition"]
        delete_set = difference["delete"]
        for number in addition_set:
            self.add_row(number)
        for number in delete_set:
            self.remove_row(number)


class CalendarScreen(Screen):
    def __init__(self):
        super(CalendarScreen, self).__init__()
        self.name = "CalendarScreen"
        self.main_layout = BoxLayout(orientation='vertical')
        self.add_widget(self.main_layout)
