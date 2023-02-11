# This program can be used to insert,update,delete and search a bookstore database

import sqlite3

class database(object):
    
    def __init__(self) -> None:
        pass

    def execute(self, command, unique, args=None):   
        global conn   
        conn = sqlite3.connect('C:\\Users\\sarad\\OneDrive\\Documents\\Hyperion DS Bootcamp\\T39\\ebookstore.db')
        cursor = conn.cursor()     

        if args is None: 
            out = cursor.execute(command)
        else:
            out = cursor.execute(command,args)
        conn.commit()
     
        if unique: 
            # list the number of records which match the select criteria to be used to check if id is unique
            print(out)
            num = list(out)      
            if num == [(1,)]:
                return True
            else:
                return False
        else:
            return out

    
    def execute_search(self,option):
        id_list = []
        title_list = []
        author_list = []

        cursor = conn.cursor()     
        cursor.execute('''SELECT * FROM books''')

        #store all records to be displayed as a search option 
        for entry in cursor:
            id_list.append(entry[0])
            title_list.append(entry[1])
            author_list.append(entry[2])    

        if option == 1:
            return title_list
        elif option == 2:
            return author_list
        elif option == 3:
            return id_list


#defining functions

def validate_id(id):
#check id is unique
    validate = database()
    command = ('''SELECT COUNT(*) from books
                    WHERE id = ?''')
    args = (id, )  

    if validate.execute(command,True,args):
        return True
    else:
        return False


#main program
ebook = database()

#create database 
command = ('''CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY, title TEXT, 
                                        author TEXT, qty INTEGER)''')

ebook.execute(command,False)

#insert records
int_rec = [(3001,'A Tale of Two Cities','Charles Dickens',30),(3002,"Harry Potter and the Philosopher's Stone",'J.K. Rowling',40),(3003,'The Lion, the Witch and the Wardrobe','C.S. Lewis',25),(3004,'The Lord of the Rings','J.R.R Tolkien',37),(3005,'Alice in Wonderland','Lewis Carroll',12)]

for r in int_rec:
    id = r[0]
    command = ('''INSERT INTO books(id,Title,Author,Qty)
                   VALUES(?,?,?,?)''')
    if not validate_id(id):
        ebook.execute(command,False,r)

#menu loop
database_active = True
while database_active:    
    choice = int(input('''
    SELECT YOUR OPTION
        0 - EXIT
        1 - ENTER BOOK
        2 - UPDATE BOOK
        3 - DELETE BOOK
        4 - SEARCH BOOK
    '''))

    if choice == 0:
        print('---GOODBYE---')
        conn.close()
        database_active = False
    

    elif choice == 1:
        new_entry = False
        while not new_entry:
            new_id = int(input(f'ENTER ID:\n'))
         
            if validate_id(new_id):
                print('id already exists, please input a unique id')
            else:
                new_entry = True

        #collect data for new record
        new_title = input(f'Title of the book?:\n')
        new_author = input(f'Author of the book:\n')
        new_qty = input(f'Quantity of book:\n')
        record = (new_id,new_title,new_author,new_qty)

        command = ('''INSERT INTO books(id,Title,Author,Qty)
                    VALUES(?,?,?,?)''')
        
        ebook.execute(command, False,record)

        print('Book sucessfully added to database')
    

    elif choice == 2:
        update_entry = False
        while not update_entry:
            id = int(input(f'Select id for book to update:\n'))

            if validate_id(id):
                 update_entry = True
            else:
                print('id does not exist, please renter id')    

        # user select what is update
        update_option = int(input(f'''What would you like to update
                                         1 - quanity
                                         2 - author
                                         3 - title\n '''))
        
        if update_option == 1:
            command = ('''UPDATE books SET Qty = ? 
                            WHERE id = ?''')
            change = int(input(f'Updated Qty:\n'))

        
        elif update_option == 2:
            command = ('''UPDATE books SET Author = ? 
                            WHERE id = ?''')
            change = input(f'Updated Author:\n')

        elif update_option == 3:
            command = ('''UPDATE books SET Title = ? 
                            WHERE id = ?''')
            change = input(f'Updated Title:\n')

        entry_details = (id,change)
        ebook.execute(command,False,entry_details)

        print('Book sucessfully updated')


    elif choice == 3:
        delete_entry = False
        while not delete_entry:
            id = int(input(f'Select id for book to delete:\n'))

            if validate_id(id):
                 delete_entry = True
            else:
                print('id does not exist, please renter id')    
        
        args = (id,)
        command = ('''DELETE FROM books
                        WHERE id = ?''')

        ebook.execute(command,False,args)
        print('Book deleted from database')


    elif choice == 4:
        entry_num = 1
        search_option = int(input(f'''SELECT SEARCH OPTION:
                                    1 - Title
                                    2 - Author
                                    3 - id\n'''))

        if search_option == 1:
            option = 1
            filter = 'title'
        if search_option == 2:
            option = 2
            filter = 'author'
        if search_option == 3:
            option = 3
            filter = 'id'

        rec_list = ebook.execute_search(option)
        for x in rec_list:        
            print(f'{entry_num} - {x}')
            entry_num += 1

        #allow user to search record using list
        user_select = int(input(f'SELECT ENTRY NUMBER FOR SEARCHING\n'))

        index = user_select - 1
        criteria = rec_list[index]
        args = (criteria,)

        command = f'''SELECT * FROM books
                        WHERE {filter} = ?'''

        for rec in ebook.execute(command,False,args):
                print(f'ID:     {rec[0]}\n')
                print(f'Title:  {rec[1]}\n')
                print(f'Author: {rec[2]}\n')
                print(f'Qty:    {rec[3]}\n')




