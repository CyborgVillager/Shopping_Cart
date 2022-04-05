'''''''''
A program that stores book information:
Title,Author
Year,ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
'''''''''
from tkinter import *
import backend


##Functions##
# binded to an widget event its called event - get_selected_row
def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        entry1.delete(0, END)
        entry1.insert(END, selected_tuple[1])
        entry2.delete(0, END)
        entry2.insert(END, selected_tuple[2])
        entry3.delete(0, END)
        entry3.insert(END, selected_tuple[3])
        entry4.delete(0, END)
        entry4.insert(END, selected_tuple[4])
        entry5.delete(0, END)
        entry5.insert(END, selected_tuple[5])
        entry6.delete(0, END)
        entry6.insert(END, selected_tuple[6])
    except IndexError:
        pass


def view_command():
    # this is an list object
    # uses viewallbt button  new rows will be put at the end of the exisiting row
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def viewcart_command():
    # this is an list object
    # uses viewallbt button  new rows will be put at the end of the exisiting row
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

"""
def search_command():
    # get info from entries
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), price_text.get(),quantity_text.get()):
        list1.insert(END, row)
"""

def add_command():
    # add info from user request
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), price_text.get(), quantity_text.get())
    list1.delete(0, END)
    # after user has inputed info , it will show as verficiation
    list1.insert(END,
                 (title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), price_text.get(), quantity_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])


def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get(),
                   price_text.get(), quantity_text.get())




def addto_cart_command():
    backend.addto_cart(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get(),
                     price_text.get(), quantity_text.get())
    list1.delete(0, END)
    # after user has inputed info , it will show as verficiation
    list1.insert(END,
                 (title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), price_text.get(),
                  quantity_text.get()))

def checkout_command():
    backend.checkout(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get(),
                     price_text.get(), quantity_text.get())


##Functions End##
# Ask user program name
# ask_user = input('Hello what would you like to name this program?')


##Top info Start##
window = Tk()
# Title for Window Screen
window.wm_title('Jonathan Almawi\'s Book Shop')
# Title
l1title = Label(window, text='Title')
l1title.grid(row=0, column=0)

# Author
l2author = Label(window, text='Author')
l2author.grid(row=0, column=2)

# ISBN
l3isbn = Label(window, text='ISBN')
l3isbn.grid(row=1, column=0)

# Year
l4year = Label(window, text='Year')
l4year.grid(row=1, column=2)

# Price
l5price = Label(window, text='Price')
l5price.grid(row=2, column=0)

# Quantity
l6quantity = Label(window, text='Quantity')
l6quantity.grid(row=2, column=2)

##Top info End##

####Entries Start####
# Title
title_text = StringVar()
# textvariable is spatial datatype
entry1 = Entry(window, textvariable=title_text)
entry1.grid(row=0, column=1)

# Author
author_text = StringVar()
entry2 = Entry(window, textvariable=author_text)
entry2.grid(row=0, column=3)

# Year
year_text = StringVar()
entry3 = Entry(window, textvariable=year_text)
entry3.grid(row=1, column=1)

# ISBN
isbn_text = StringVar()
entry4 = Entry(window, textvariable=isbn_text)
entry4.grid(row=1, column=3)

# Price
price_text = StringVar()
entry5 = Entry(window, textvariable=price_text)
entry5.grid(row=2, column=1)

# Quantity
quantity_text = StringVar()
entry6 = Entry(window, textvariable=quantity_text)
entry6.grid(row=2, column=3)

# List Box
# box width and height
list1 = Listbox(window, height=12, width=70)
list1.grid(row=3, column=0, rowspan=6, columnspan=2)
####Entries End####

###Scroll Bar Start###
# scrollbar location
scrollbar1 = Scrollbar(window)
scrollbar1.grid(row=2, column=2, rowspan=6)  # rowspan - centered

# Apply scrollbar config to list
list1.configure(yscrollcommand=scrollbar1.set)
scrollbar1.configure(command=list1.yview)
# Binding the list t get the the selected row
# From user input
list1.bind('<<ListboxSelect>>', get_selected_row)

###Scroll Bar End###


####Button Start####
# View All
viewallbt = Button(window, text='View all Books', width=12, command=view_command)
viewallbt.grid(row=3, column=3)

"""
# Search Entry
searchbt = Button(window, text='Search Entry', width=12, command=search_command)
searchbt.grid(row=4, column=3)
"""
# Add entry
entrybt = Button(window, text='Add Books', width=12, command=add_command)
entrybt.grid(row=4, column=3)

# Update Book Info
updatebt = Button(window, text='Update Books', width=12, command=update_command)
updatebt.grid(row=5, column=3)

# Add to Cart
addtocartbt = Button(window, text='Add to Cart', width=12, command=addto_cart_command)
addtocartbt.grid(row=6, column=3)

# Checkout
checkoutbt = Button(window, text='Checkout Cart', width=12, command=checkout_command)
checkoutbt.grid(row=7, column=3)

# Delete Book Button
deletebt = Button(window, text='Delete Selected', width=12, command=delete_command)
deletebt.grid(row=8, column=3)

# Close
closebt = Button(window, text='Exit', width=12, command=window.destroy)
closebt.grid(row=9, column=3)

####Button End####

# wrap all all widgets
window.mainloop()
