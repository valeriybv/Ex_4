from constants import directories


class Directories(object):
    def __init__(self, number):
        self.number = number
        self.documents = []

    def add_document(self, document):
        try:
            self.documents.append(document)
        except:
            print("Error")

    def get_directory_by_docnum(self, docnum):
        for k, v in directories.items():
            if docnum in v:
                return k

