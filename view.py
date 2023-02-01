import controller
from tkinter import *

def set_new_contact():
    elements = controller.get_elements()
    name = elements['name'].get()
    surname = elements['surname'].get()
    number = elements['number'].get()
    contact = f'{name} {surname} : {number}'
    controller.add_to_listbox(contact)
    
def print_contacts_list(contacts_list):
    for contact in contacts_list:
        #print(contact)
        #if contact != ' ':
        controller.add_to_listbox(contact)