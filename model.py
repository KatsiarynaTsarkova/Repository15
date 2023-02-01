import view

def write_contacts(contacts_list):
    data = open('archive.txt', mode ='w', encoding = 'utf-8')
    for contacts in contacts_list:
        data.writelines(contacts + '\n')
    data.close()
    
def read_contacts():
    data = open('archive.txt', mode ='r', encoding = 'utf-8')
    contacts_list = data.readlines()
    view.print_contacts_list(contacts_list)
    data.close()     