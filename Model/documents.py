from constants import documents
import View.exceptions as errors


class Documents(object):
    def __init__(self, type, number, name, directory):
        self.type = type
        self.number = number
        self.name = name
        self.directory = directory

    @staticmethod
    def create_item(type, number, name, shelve):
        documents.append({'type': type, 'number': number, 'name': name})

    @staticmethod
    def get_document_by_number(number):
        result = list(filter(lambda x: x['number'] == number, documents))
        if result:
            return result[0]
        else:
            errors.document_not_found()

    def get_owner(self, number):
        doc = self.get_document_by_number(number)
        try:
            return doc['name']
        except:
            pass

    def get_documents(self):
        return [doc for doc in documents]
