from Model.documents import Documents
from constants import documents
from View import prints

command = input("Введите комманду:")
while command != 'q':
    if command == '/h':
        prints.print_available_commands()
    elif command == 'p':
        number = input("Введите номер документа:")
        name = Documents.get_owner(Documents, number)
        prints.print_document_owner(name)
    else:
        prints.wrong_command()
    command = input("Введите комманду:")


