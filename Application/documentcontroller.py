from Model.documents import Documents
from Model.directories import Directories
import View


class DocumentController(object):
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def validate_document(doc):
        dir = Directories.get_directory_by_number(Directories, doc.directory)
        if (dir is None):
            View.exceptions.directory_not_exist()
        else:
            return True

    def add_document(self, doc):
        if(self.validate_document(doc) == True):
            Documents.add_document(doc)
            Directories.apply_book_to_directory(doc.directory, doc.number)
        pass
    @staticmethod
    def remove_document(docnum):
        try:
            doc = Documents.get_document_by_number(docnum)
            Documents.remove_document(doc)
        except:
            pass