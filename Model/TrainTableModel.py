from TrainTableNote import TrainTableNote
from datetime import date, datetime, time, timedelta


class TrainTableModel:
    def __init__(self):
        self.trains: list = []

    def add_new_train_note(self,
                           start_station,
                           end_station,
                           start_datetime: datetime,
                           end_datetime: datetime,
                           ):
        self.trains.append(TrainTableNote(start_station,
                                          end_station,
                                          start_datetime,
                                          end_datetime))

    def find_with_train_number(self,
                               search_number):
        if search_number > len(self.trains):
            return []
        return [search_number - 1]

    def find_with_start_date(self,
                             search_start_date: date):
        search_result = []
        for index in range(len(self.trains)):
            if self.trains[index].start_datetime.date() == search_start_date:
                search_result.append(index)
        return search_result

    def find_in_time_range(self,
                           low_time_level: time,
                           top_time_level: time,
                           search_parameter):
        search_result = []
        for index in range(len(self.trains)):
            current_train_time = self.trains[index].__dict__[search_parameter].time()
            if low_time_level >= current_train_time >= top_time_level:
                search_result.append(index)
        return search_result

    def find_with_station(self,
                          search_station,
                          search_parameter):
        search_result = []
        for index in range(len(self.trains)):
            current_train_station = self.trains[index].__dict__[search_parameter]
            if current_train_station == search_station:
                search_result.append(index)
        return search_result

    def find_with_path_time(self, search_path_time: timedelta):
        search_result = []
        for index in range(len(self.trains)):
            if self.trains[index].path_time == search_path_time:
                search_result.append(index)
        return search_result

    def delete_notes(self, list_of_deleting_indexes: list):
        list_of_deleting_indexes.sort(reverse=True)
        for index in list_of_deleting_indexes:
            self.trains.pop(index)
