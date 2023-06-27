from Model.documents import Documents
from Model.directories import Directories
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
        pass
    elif command == 'ds':
        pass
    elif command == 'ad':
        pass
    elif command == 'd':
        pass
    elif command == 'm':
        pass
    else:
        prints.wrong_command()
    command = input("Введите комманду:")


