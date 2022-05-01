from xml.dom.minidom import getDOMImplementation


class TrainDomWriter:
    necessary_data_tag_names = ["start_station",
                                "end_station",
                                "start_datetime",
                                "end_datetime"]

    def __init__(self):
        self.implementation = getDOMImplementation()
        self.current_data = list()
        self.current_document = None

    def set_data(self,
                 current_data):
        self.current_data = list(current_data)

    def create_new_document(self):
        new_document = self.implementation.createDocument(None,
                                                          "trains",
                                                          None)
        document_element = new_document.documentElement
        for train_data in self.current_data:
            train = new_document.createElement("train")
            for tag_name, element_data in zip(TrainDomWriter.necessary_data_tag_names,
                                              train_data):
                train_attribute = new_document.createElement(tag_name)
                train_attribute.appendChild(new_document.createTextNode(element_data))
                train.appendChild(train_attribute)
            document_element.appendChild(train)
        self.current_document = new_document

    def write_current_document_to_file(self,
                                       filename):
        self.current_document.writexml(open(filename, "w"),
                                       indent="  ",
                                       addindent="  ",
                                       newl="\n")

    def create_and_write(self,
                         current_data,
                         filename):
        self.set_data(current_data)
        self.create_new_document()
        self.write_current_document_to_file(filename)
