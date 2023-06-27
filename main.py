from Model.documents import Documents
from Model.directories import Directories
from Application.documentcontroller import DocumentController
from View import prints

command = input("Введите комманду:")
while command != 'q':
    if command == '/h':
        prints.print_available_commands()
    elif command == 'p':
        number = input("Введите номер документа:")
        name = Documents.get_owner(Documents, number)
        if name:
            prints.print_document_owner(name)
    elif command == 's':
        docnum = input("Введите номер документа:")
        doc = Documents.get_document_by_number(docnum)
        if doc:
            dir = Directories.get_directory_by_docnum(Directories, docnum)
            prints.print_document_directory(dir)
    elif command == 'l':
        docs = Documents.get_documents(Documents)
        if docs:
            for d in docs:
                d['directory'] = Directories.get_directory_by_docnum(Directories, d['number'])
            prints.print_document_list(docs)
    elif command == 'ads':
        number = input("Введите номер полки:")
        Directories.add_directory(Directories, number)
        prints.print_directories_list(Directories.get_directories(Directories))
    elif command == 'ds':
        dirnum = input("Введите номер полки:")
        Directories.remove_directory(Directories, dirnum)
        prints.print_directories_list(Directories.get_directories(Directories))
        pass
    elif command == 'ad':
        type = input("Введите тип документа:")
        number = input("Введите номер документа:")
        name = input("Введите владельца документа:")
        directory = input("Введите номер папки:")

        newdoc = Documents(type, number, name, directory)
        DocumentController.add_document(DocumentController, newdoc)
    elif command == 'd':
        number = input("Введите номер документа для удаления:")
        DocumentController.remove_document(number)
        pass
    elif command == 'm':
        pass
    else:
        prints.wrong_command()
    command = input("Введите комманду:")


