import xml.sax
from xml.sax.__init__ import SAXParseException


class TrainSaxHandler(xml.sax.handler.ContentHandler):
    necessary_data_tag_names = ["start_station",
                                "end_station",
                                "start_datetime",
                                "end_datetime"]
    unnecessary_content = ["    ", '      ', "\n"]

    def __init__(self,
                 reader):
        super(TrainSaxHandler, self).__init__()
        self.reader = reader
        self.current_data = list()
        self.current_tag = ""

    def startElement(self,
                     tag,
                     attrs):
        self.current_tag = tag

    def characters(self,
                   content):
        if self.current_tag in TrainSaxHandler.necessary_data_tag_names:
            if content not in TrainSaxHandler.unnecessary_content:
                self.current_data.append(content)

    def endElement(self,
                   tag):
        if tag == "train":
            self.reader.general_data.append(tuple(self.current_data))
            self.current_data.clear()


class TrainSaxReader:
    def __init__(self):
        self.general_data = list()
        self.parser = xml.sax.make_parser()
        self.parser.setContentHandler(TrainSaxHandler(self))

    def parse(self,
              filename):
        try:
            self.parser.parse(filename)
        except SAXParseException:
            return

    def get_general_data(self):
        return list(self.general_data)
