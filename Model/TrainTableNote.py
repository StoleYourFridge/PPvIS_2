from datetime import datetime


class TrainTableNote:
    def __init__(self,
                 train_number,
                 start_station,
                 end_station,
                 start_datetime,
                 end_datetime):
        self.train_number = train_number
        self.start_station = start_station
        self.end_station = end_station
        self.start_datetime: datetime = start_datetime
        self.end_datetime: datetime = end_datetime
        self.path_time = self.end_datetime - self.start_datetime

    def get_train_note_info(self):
        result = (str(self.train_number),
                  self.start_station,
                  self.end_station,
                  str(self.start_datetime),
                  str(self.end_datetime),
                  str(self.path_time))
        return result
