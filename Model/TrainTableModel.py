from Model.TrainTableNote import TrainTableNote
from datetime import date, datetime, time, timedelta


class TrainTableModel:
    def __init__(self):
        self.train_id = 0
        self.existing_ids = set()
        self.trains: list = []

    def add_new_train_note(self,
                           start_station,
                           end_station,
                           start_datetime: datetime,
                           end_datetime: datetime,
                           ):
        self.increase_train_id()
        self.existing_ids.add(self.train_id)
        self.trains.append(TrainTableNote(self.train_id,
                                          start_station,
                                          end_station,
                                          start_datetime,
                                          end_datetime))

    def find_with_train_number(self,
                               search_train_number):
        for train_note in self.trains:
            if train_note.train_number == search_train_number:
                return {search_train_number}
        return set()

    def find_with_date(self,
                       search_date: date,
                       search_parameter):
        search_result = set()
        for train_note in self.trains:
            if train_note.__dict__[search_parameter].date() == search_date:
                search_result.add(train_note.train_number)
        return search_result

    def find_in_time_range(self,
                           low_time_level: time,
                           top_time_level: time,
                           search_parameter):
        search_result = set()
        for train_note in self.trains:
            current_train_time = train_note.__dict__[search_parameter].time()
            if low_time_level <= current_train_time <= top_time_level:
                search_result.add(train_note.train_number)
        return search_result

    def find_with_station(self,
                          search_station,
                          search_parameter):
        search_result = set()
        for train_note in self.trains:
            current_train_station = train_note.__dict__[search_parameter]
            if current_train_station == search_station:
                search_result.add(train_note.train_number)
        return search_result

    def find_with_path_time(self, search_path_time: timedelta):
        search_result = set()
        for train_note in self.trains:
            if train_note.path_time == search_path_time:
                search_result.add(train_note.train_number)
        return search_result

    def delete_notes(self, set_of_deleting_train_numbers):
        self.existing_ids.difference_update(set_of_deleting_train_numbers)
        for deleting_train_number in set_of_deleting_train_numbers:
            for index in range(len(self.trains)):
                if self.trains[index].train_number == deleting_train_number:
                    self.trains.pop(index)
                    break

    def increase_train_id(self):
        self.train_id += 1

    def get_train_note_info_with_number(self, number):
        for train_note in self.trains:
            if train_note.train_number == number:
                return train_note.get_train_note_info()
        return ()
