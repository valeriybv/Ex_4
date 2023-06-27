from constants import directories
import View.exceptions as errors


class Directories(object):
    def __init__(self, number):
        self.number = number
        self.documents = []

    def get_directory_by_docnum(self, docnum):
        for k, v in directories.items():
            if docnum in v:
                return k

    def get_directory_by_number (self, number):
        for k, v in directories.items():
            if number in k:
                return k, v

    def get_directory_books(self, dirnum):
        try:
            dir = self.get_directory_by_number(self, dirnum)
            books = dir[1]
            return books
        except:
            errors.directory_not_exist()

    def get_directories(self):
        return sorted([dir for dir in directories])

    def add_directory(self, number):
        if(self.get_directory_by_number(self, number)):
            errors.directory_already_exists()
        else:
            directories[number] = []

    def remove_directory(self, dirnum):
        dir = self.get_directory_by_number(self, dirnum)
        try:
            if(self.get_directory_books(self, dirnum)):
                errors.directory_not_empty()
            else:
                del directories[dirnum]
        except:
            pass
