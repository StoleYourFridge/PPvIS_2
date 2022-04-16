from datetime import datetime


class TrainNote:
    def __init__(self,
                 start_station,
                 end_station,
                 start_datetime,
                 end_datetime):
        self.start_station = start_station
        self.end_station = end_station
        self.start_datetime: datetime = start_datetime
        self.end_datetime: datetime = end_datetime
        self.path_time = self.end_datetime - self.start_datetime

    def get_train_note_info(self):
        result = (self.start_station, self.end_station, self.start_datetime, self.end_datetime)
        return result
