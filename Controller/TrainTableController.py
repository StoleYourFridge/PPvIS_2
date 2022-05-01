from Model.TrainTableModel import TrainTableModel
from datetime import date, time, datetime, timedelta
from FileManagement.TrainDomWriter import TrainDomWriter
from FileManagement.TrainSaxReader import TrainSaxReader
import os
FILE_DATA_PATH = "FileData"
MINIMUM_FILENAME_SIZE = 5


class TrainTableController:
    def __init__(self):
        self.model = TrainTableModel()
        self.current_search_version = set()
        self.corrected_search_version = set()
        self.current_table_version = set()
        self.corrected_table_version = self.model.existing_ids

    def add_new_note_validated(self,
                               start_station,
                               end_station,
                               start_date,
                               start_time,
                               end_date,
                               end_time):
        if start_station == "" or end_station == "":
            return False
        if start_station == end_station:
            return False
        start_datetime = start_date + " " + start_time
        end_datetime = end_date + " " + end_time
        try:
            start_datetime = datetime.fromisoformat(start_datetime)
            end_datetime = datetime.fromisoformat(end_datetime)
        except ValueError:
            return False
        else:
            if start_datetime >= end_datetime:
                return False
            self.model.add_new_train_note(start_station,
                                          end_station,
                                          start_datetime,
                                          end_datetime)
            return True

    def find_with_train_number_validated(self,
                                         search_number):
        try:
            search_number = int(search_number)
        except ValueError:
            return False
        else:
            self.corrected_search_version = self.model.find_with_train_number(search_number)
            return True

    def find_with_start_date_validated(self,
                                       search_start_date):
        try:
            search_start_date = date.fromisoformat(search_start_date)
        except ValueError:
            return False
        else:
            self.corrected_search_version = self.model.find_with_date(search_start_date,
                                                                      "start_datetime")
            return True

    def find_with_end_date_validated(self,
                                     search_end_date):
        try:
            search_start_date = date.fromisoformat(search_end_date)
        except ValueError:
            return False
        else:
            self.corrected_search_version = self.model.find_with_date(search_start_date,
                                                                      "end_datetime")
            return True

    def find_in_start_time_range_validated(self,
                                           low_time_level,
                                           top_time_level):
        try:
            low_time_level = time.fromisoformat(low_time_level)
            top_time_level = time.fromisoformat(top_time_level)
        except ValueError:
            return False
        else:
            self.corrected_search_version = self.model.find_in_time_range(low_time_level,
                                                                          top_time_level,
                                                                          "start_datetime")
            return True

    def find_in_end_time_range_validated(self,
                                         low_time_level,
                                         top_time_level):
        try:
            low_time_level = time.fromisoformat(low_time_level)
            top_time_level = time.fromisoformat(top_time_level)
        except ValueError:
            return False
        else:
            self.corrected_search_version = self.model.find_in_time_range(low_time_level,
                                                                          top_time_level,
                                                                          "end_datetime")
            return True

    def find_with_start_station_validated(self,
                                          search_station):
        self.corrected_search_version = self.model.find_with_station(search_station,
                                                                     "start_station")
        return True

    def find_with_end_station_validated(self,
                                        search_station):
        self.corrected_search_version = self.model.find_with_station(search_station,
                                                                     "end_station")
        return True

    def find_with_path_time_validated(self,
                                      path_days,
                                      path_hours,
                                      path_minutes,
                                      path_seconds):
        try:
            path_days = int(path_days)
            path_hours = int(path_hours)
            path_minutes = int(path_minutes)
            path_seconds = int(path_seconds)
        except ValueError:
            return False
        else:
            search_path_time = timedelta(days=path_days,
                                         hours=path_hours,
                                         minutes=path_minutes,
                                         seconds=path_seconds)
            self.corrected_search_version = self.model.find_with_path_time(search_path_time)
            return True

    def delete_notes_with_buffer(self):
        self.model.delete_notes(self.corrected_search_version)

    def delete_all_notes(self):
        self.model.delete_notes(self.corrected_table_version)

    @staticmethod
    def get_update_difference(updated_ids_set: set,
                              current_output_ids_set: set):
        addition_set = updated_ids_set.difference(current_output_ids_set)
        delete_set = current_output_ids_set.difference(updated_ids_set)
        return {"addition": addition_set, "delete": delete_set}

    def get_main_screen_difference(self):
        difference = self.get_update_difference(self.corrected_table_version,
                                                self.current_table_version)
        self.current_table_version = set(self.corrected_table_version)
        return difference

    def get_search_screen_difference(self):
        difference = self.get_update_difference(self.corrected_search_version,
                                                self.current_search_version)
        self.current_search_version = set(self.corrected_search_version)
        return difference

    @staticmethod
    def filename_validation(filename):
        if len(filename) < MINIMUM_FILENAME_SIZE:
            return False
        elif filename[-1:-5:-1] != "lmx.":
            return False
        return True

    @staticmethod
    def add_new_file(new_filename):
        if not TrainTableController.filename_validation(new_filename):
            return False
        if new_filename not in set(os.listdir(FILE_DATA_PATH)):
            new_file = open(FILE_DATA_PATH + "/" + new_filename, "w")
            new_file.close()
            return True
        else:
            return False

    @staticmethod
    def delete_file(filename):
        if not TrainTableController.filename_validation(filename):
            return False
        if filename in set(os.listdir(FILE_DATA_PATH)):
            os.remove(FILE_DATA_PATH + "/" + filename)
            return True
        return False

    def read_from_file(self,
                       filename):
        if filename not in set(os.listdir(FILE_DATA_PATH)):
            return False
        reader = TrainSaxReader()
        reader.parse(FILE_DATA_PATH + "/" + filename)
        train_data = reader.get_general_data()
        for train in train_data:
            self.model.add_new_train_note(train[0],
                                          train[1],
                                          datetime.fromisoformat(train[2]),
                                          datetime.fromisoformat(train[3]))
        return True

    def write_to_file(self,
                      filename):
        if filename not in set(os.listdir(FILE_DATA_PATH)):
            return False
        trains = []
        for train_number in self.corrected_table_version:
            train_data = self.model.get_train_note_info_with_number(train_number)
            trains.append(train_data[1:5:1])
        writer = TrainDomWriter()
        writer.create_and_write(trains, FILE_DATA_PATH + "/" + filename)
        return True
