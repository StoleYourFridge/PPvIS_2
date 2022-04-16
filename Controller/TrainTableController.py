from Model.TrainTable import TrainTable
from datetime import datetime, timedelta, time, date


class TrainTableController:
    def __init__(self):
        self.model = TrainTable()
        self.search_buffer = []

    def clear_search_buffer(self):
        self.search_buffer.clear()

    def add_new_note_validated(self,
                               start_station,
                               end_station,
                               start_datetime: datetime,
                               end_datetime: datetime):
        if start_station == end_station:
            return False
        if start_datetime >= end_datetime:
            return False
        self.model.add_new_train_note(start_station,
                                      end_station,
                                      start_datetime,
                                      end_datetime)
        return True

    def find_with_train_number_validated(self, search_number):
        try:
            train_number = int(search_number)
        except ValueError:
            return False
        else:
            self.search_buffer = self.model.find_with_train_number(search_number)
            return True

    def find_with_start_date_validated(self, search_start_date):
        self.search_buffer = self.model.find_with_start_date(search_start_date)
        return True

    def find_in_start_time_range_validated(self, low_time_level, top_time_level):
        self.search_buffer = self.model.find_in_time_range(low_time_level, top_time_level, "start_datetime")
        return True

    def find_in_end_time_range_validated(self, low_time_level, top_time_level):
        self.search_buffer = self.model.find_in_time_range(low_time_level, top_time_level, "end_datetime")
        return True

    def find_with_start_station_validated(self, search_station):
        self.search_buffer = self.model.find_with_station(search_station, "start_station")
        return True

    def find_with_end_station_validated(self, search_station):
        self.search_buffer = self.model.find_with_station(search_station, "end_station")
        return True

    def find_with_path_time_validated(self, search_path_time):
        self.search_buffer = self.model.find_with_path_time(search_path_time)
        return True

    def delete_notes_with_buffer(self):
        self.model.delete_notes(self.search_buffer)
        self.clear_search_buffer()
        return True
