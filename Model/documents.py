from constants import documents


class Documents(object):
    def __init__(self, type, number, name, shelve):
        self.type = type
        self.number = number
        self.name = name
        self.shelve = shelve

    def create_item(self, type, number, name, shelve):
        documents.append({'type': type, 'number': number, 'name': name})

    def get_document_by_number(self, number):
        result = list(filter(lambda x: x['number'] == number, documents))
        if result:
            return result[0]
        else:
            print("Error")
    def get_owner(self, number):
        doc = self.get_document_by_number(self, number)
        return doc['name']
