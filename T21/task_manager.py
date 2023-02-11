
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

class Task:
    def __init__(self, task_num = None, username = None, title = None, description = None, due_date = None, assigned_date = None, completed = None):
        '''
        Inputs:
        task_num: Integer
        username: String
        title: String
        description: String
        due_date: DateTime
        assigned_date: DateTime
        completed: Boolean
        '''
        self.task_num = task_num
        self.username = username
        self.title = title
        self.description = description
        self.due_date = due_date
        self.assigned_date = assigned_date
        self.completed = completed

    def __str__(self) -> str:
        return str(self.__init__(self.completed))

        
        
    def from_string(self, task_str):
        '''
        Convert from string in tasks.txt to object
        '''
        tasks = task_str.split(",")
        task_num = tasks[0]
        username = tasks[1]
        title = tasks[2]
        description = tasks[3]
        due_date = datetime.strptime(tasks[4], DATETIME_STRING_FORMAT)
        assigned_date = datetime.strptime(tasks[5], DATETIME_STRING_FORMAT)
        completed = True if tasks[6] == "Yes" else False
        self.__init__(task_num, username, title, description, due_date, assigned_date, completed)


    def to_string(self):
        '''
        Convert to string for storage in tasks.txt
        '''
        str_attrs = [
            self.task_num,
            self.username,
            self.title,
            self.description,
            self.due_date.strftime(DATETIME_STRING_FORMAT),
            self.assigned_date.strftime(DATETIME_STRING_FORMAT),
            "Yes" if self.completed else "No"
        ]
        return ",".join(str_attrs)

    def display(self):
        '''
        Display object in readable format
        '''
        disp_str = f"------------- {self.task_num} --------------\n"
        disp_str += f"Task: \t\t {self.title}\n"
        disp_str += f"Assigned to: \t {self.username}\n"
        disp_str += f"Date Assigned: \t {self.assigned_date.strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {self.due_date.strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n{self.description}\n"
        return disp_str

# Read and parse tasks.txt
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = Task()
    curr_t.from_string(t_str)
    task_list.append(curr_t)

# Read and parse user.txt

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(";")
    username_password[username] = password

# Keep trying until a successful login
logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

def validate_string(input_str):
    '''
    Function for ensuring that string is safe to store
    '''
    if ";" in input_str:
        print("Your input cannot contain a ';' character")
        return False
    return True

def check_username_and_password(username, password):
    '''
    Ensures that usernames and passwords can't break the system
    '''
    # ';' character cannot be in the username or password
    if ";" in username or ";" in password:
        return False
    return True

def write_usernames_to_file(username_dict):
    '''
    Function to write username to file

    Input: dictionary of username-password key-value pairs
    '''
    with open("user.txt", "w") as out_file:
        user_data = []
        for k in username_dict:
            user_data.append(f"{k};{username_dict[k]}")
        out_file.write("\n".join(user_data))
  
        
def name_check(name_to_check):
    ''' check if username exist '''
    if name_to_check in username_password:
        return True
    else:
        return False


def reg_user(user_name,password):
        ''' This function registers new users '''
        # Request input of a new username
        if curr_user != 'admin':
            print("Registering new users requires admin privileges")
            return
        if not check_username_and_password(new_username, new_password):
            # Username or password is not safe for storage - continue
            print("Username or password cannot contain ';'.")
            return
        # Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # Check if the new password and confirmed password are the same.
        if password == confirm_password:
        # check that username is unique else show message
            user_name_lower = str(user_name).lower()
            if not name_check(user_name_lower):
            # If they are the same, add them to the user.txt file,
                print("New user added")

            # Add to dictionary and write to file               
                username_password[user_name] = password
                write_usernames_to_file(username_password)
            else:
                print('Duplicate: User already registered - CHOOSE NEW USERNAME AND PASSWORD')
                second_username = input('New Username: ')
                second_password = input('New Password: ')
                reg_user(second_username,second_password)
        # Otherwise you present a relevant message.
        else:
            print("Passwords do no match")

def add_task(task_username):
        '''This function creates new tasks'''
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
        #swapped continue with return as continue is only for loops - hopefully thus does the same thing
            return
        
        # new task number
        num = len(task_list) + 1
        task_num = f'Task {num}'

        # Get title of task and ensure safe for storage
        while True:
            task_title = input("Title of Task: ")
            if validate_string(task_title):
                break

        # Get description of task and ensure safe for storage
        while True:
            task_description = input("Description of Task: ")
            if validate_string(task_description):
                break

        # Obtain and parse due date
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break
            except ValueError:
                print("Invalid datetime format. Please use the format specified")

        # Obtain and parse current date
        curr_date = date.today()
        
        # Create a new Task object and append to list of tasks
        new_task = Task(task_num,task_username, task_title, task_description, due_date_time,curr_date, False)
        task_list.append(new_task)

        # Write to tasks.txt
        with open("tasks.txt", "w") as task_file:
            task_file.write("\n".join([t.to_string() for t in task_list]))
        print("Task successfully added.")  

def view_all():
        ''' This function allows the user to view all tasks'''
        print("-----------------------------------")

        if len(task_list) == 0:
            print("There are no tasks.")
            print("-----------------------------------")

        for t in task_list:
            print(t.display())
            print("-----------------------------------")  

def view_mine():
        ''' This function allows the user to view their own tasks'''
        print("-----------------------------------")
        has_task = False
        for t in task_list:
            if t.username == curr_user:
                has_task = True
                print(t.display())
                print("-----------------------------------")

        if not has_task:
            print("You have no tasks.")
            print("-----------------------------------")
        else:
#this is to allow the user to seach a task by number once their own has been viewed and edit or mark task as complete
            check_task_option = True
            while check_task_option:
              check_task_num = int(input('''1. search by task\n-1. to return to menu\n'''))
              if check_task_num == 1:
                 user_num = int(input('Enter task number: '))                
                 if task_by_number(user_num):                   
                    check_task_option = False

              elif check_task_num == -1:
                return

              else:
                print('Invalid Option Selected')
                return
              
              task_action = True
              while task_action:
                action = int(input('''1. Mark task complete \n2. Edit Task\n-1. return to menu\n'''))
                if action == 1:
                   complete_task(user_num)
                   task_action = False

                elif action == 2:
                   edit_task(user_num)
                   task_action = False

                elif action == -1:
                   return
                else:
                   print('Invalid Option Selected')
 

def task_by_number(task_number):
    '''This function allows the user to view by task number'''
    task_found = False
    task_number -= 1

    if task_number >=0 and task_number < len(task_list):
        searched_task = task_list[task_number]
        print(searched_task.display())
        print("-----------------------------------")
        task_found = True
        
    if not task_found:
        print('''This task number doesn't exist''')
        print("-----------------------------------")
        return(False)
    
def complete_task(task_number_complete):
        '''This function changes the task to complete'''

        with open('tasks.txt', 'r') as task_file:
            for record in task_file:
                record_split = record.split(',')
                if record_split[0] == f'Task {task_number_complete}':
                    if record_split[6] == 'No':
                        task_number_complete -= 1
                        record_split_4 = datetime.strptime(record_split[4],DATETIME_STRING_FORMAT)
                        record_split_5 = datetime.strptime(record_split[5],DATETIME_STRING_FORMAT)
                        task_list[task_number_complete] = Task(record_split[0],record_split[1],record_split[2],record_split[3],record_split_4,record_split_5,True)
                        #clear the file and read the tasks with the changes in order from task_list
                        update_task()
                        print('Task is now marked as complete')
                    else:
                        print('Task is already marked as complete')
                        


def edit_task(task_number_edit):
    ''' This function allows the user to edit the task '''
    edited_date = False
    edited_task = False
    name_valid = False

    user_choice = input('''Would you like to edit\nnm - Name of task owner\ndd - Due date\n''')

    with open('tasks.txt', 'r') as task_file:
        for entry in task_file:
            entry_split = entry.split(',')
            if entry_split[0] == f'Task {task_number_edit}':
                task_to_edit = entry_split
    
    while not edited_task:
        if user_choice == 'nm':
            while not name_valid:
                new_name = str(input('Name new: '))
             #check if name exists if so change it else ask them to register a new user
                if name_check(new_name.lower()):
                   print('here')
                   task_to_edit[1] = new_name
                   edited_task = True
                   name_valid = True
                else:
                   print('Name not registered - try again')
        
   
            
        elif user_choice == 'dd':
            new_due_date = input("New due date of task (YYYY-MM-DD): ")
            new_due_date_time = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
            task_to_edit[4] = new_due_date_time
            edited_date = True
            edited_task = True
            
        else:
            print('Invalid option selected')


    #putting the date into the correct format to pass it as an argument in the class        
    task_to_edit_5 = datetime.strptime(task_to_edit[5], DATETIME_STRING_FORMAT)
    if edited_date:
       task_to_edit_4 = new_due_date_time
    else:
       task_to_edit_4 = datetime.strptime(task_to_edit[4], DATETIME_STRING_FORMAT)
    #checking if task is complete or not to pass the correct boolean value
    if task_to_edit[6] == 'Yes':
        task_to_edit_6 = True
    else:
        task_to_edit_6 = False

    task_number_edit -= 1    
    task_list[task_number_edit] = Task(task_to_edit[0],task_to_edit[1],task_to_edit[2],task_to_edit[3],task_to_edit_4,task_to_edit_5,task_to_edit_6)
    #clear the file and read the tasks with the changes in order from task_list
    update_task()
    print('Task has been sucessfully edited')

def update_task():
    '''This method clears and rewrites the text file with the updates'''
    with open('tasks.txt','r+') as task_file:
        task_file.truncate(0)
        for t in task_list:
            task_file.write(f'{t.to_string()}\n')

def task_overview():
    ''' This method generates a report which gives an overview of the tasks in the manager'''
    total_tasks = len(task_list)
    not_completed_tasks = completed_tasks = incomplete_overdue = overdue_tasks = 0         
    today_date = datetime.now()
    with open('tasks.txt','r') as task_file:
        file_whole = task_file.read()
        record = file_whole.split('\n')

    for j in range(0,len(record)):
        task = str(record[j]).split(',')

# number of complete and incomplete tasks
        if task[6] == 'Yes':
           completed_tasks +=1
        else:
           not_completed_tasks += 1

# number of incomplete and overdue tasks
        check_due_date = datetime.strptime(task[4], DATETIME_STRING_FORMAT) 
        if task[6] == 'No' and  check_due_date < today_date:
            incomplete_overdue += 1

# number of overdue tasks
        if check_due_date < today_date:
            overdue_tasks += 1

#percentage of incomplete tasks
    percentage_incomplete_tasks = round((not_completed_tasks /len(task_list)) * 100,2)
 
#percentage of overdue tasks
    percentage_overdue_tasks = round((overdue_tasks / len(task_list)) * 100,2)

# string together report details
    t_overview_str = '---------- TASK OVERVIEW REPORT ----------\n'
    t_overview_str += f'{today_date}\n'
    t_overview_str += f'Total no. of Tasks: {total_tasks}\n'
    t_overview_str += f'No. of Completed Tasks: {completed_tasks}\n'
    t_overview_str += f'No. of Incomplete Tasks: {not_completed_tasks}\n'
    t_overview_str += f'No. of Incomplete and Overdue Tasks: {incomplete_overdue}\n'
    t_overview_str += f'No. of Overdue Tasks: {overdue_tasks}\n'
    t_overview_str += f'% of Incomplete Tasks: {percentage_incomplete_tasks}\n'
    t_overview_str += f'% of Overdue Tasks {percentage_overdue_tasks}\n'

    with open('task_overview.txt','w') as task_report:
        task_report.write(t_overview_str)

def user_overview():
    '''This method generates a report at about users'''
    num_reg_user = len(username_password)
    num_of_tasks = len(task_list)
    tasks_per_user = {}
    percent_complete_per_user = {}
    percent_incomplete_per_user = {}
    percent_incomp_overdue_per_user = {}
    percent_task_per_person = {}

    todays_date = datetime.now()
    #calculating the number of tasks per user
    with open('tasks.txt','r') as task_file:
        file_whole = task_file.read()
        record = file_whole.split('\n')

    for user in username_password.keys():
        single_task = single_incomplete_task = single_complete_task = single_incomplete_overdue = 0
        for j in range(0,len(record)):
          task = record[j].split(',')
          if task[1] == user:
            single_task += 1
            if task[6] == 'Yes':
        # number of complete tasks
                single_complete_task += 1
            else:
        # number of incomplete tasks
                single_incomplete_task += 1
        # number of incomplete and overdue tasks
            check_due_date = datetime.strptime(task[4], DATETIME_STRING_FORMAT)
            if task[6] == 'No' and  check_due_date < todays_date:
               single_incomplete_overdue += 1

        tasks_per_user[user] = single_task
        #is there are no tasks assigned to the user, don't calculate statistics
        if single_task == 0: 
            percent_task_per_person[user] = 'N/A'
            percent_complete_per_user[user] = 'N/A'
            percent_incomplete_per_user[user] = 'N/A'
            percent_incomp_overdue_per_user[user] = 'N/A'
        else:
            percent_task_per_person[user] = round((single_task/num_of_tasks) * 100,2)
            percent_complete_per_user[user] = round((single_complete_task/single_task) * 100,2)
            percent_incomplete_per_user[user] = round((single_incomplete_task/single_task) * 100,2)
            percent_incomp_overdue_per_user[user] = round((single_incomplete_overdue/single_task) * 100,2)

# printing report
    u_overview_str = '---------- USER OVERVIEW REPORT ----------\n'
    u_overview_str += f'Number of Registered Users: {num_reg_user}\n'
    u_overview_str += f'Number of Tasks: {num_of_tasks}\n'

    with open('user_overview.txt','w') as user_report:
        user_report.write(u_overview_str)
        for u_print in username_password.keys():
            u_str = '\n------------------------------------------------\n'
            u_str += f'USERNAME: {u_print}\n'
            u_str += f'Number of Tasks: {tasks_per_user[u_print]}\n'
            u_str += f'% of Total Tasks: {percent_task_per_person[u_print]}\n'
            u_str += f'% of Completed Tasks: {percent_complete_per_user[u_print]}\n'
            u_str += f'% of Incomplete Tasks: {percent_incomplete_per_user[u_print]}\n'
            u_str += f'% of Incomplete and Overdue Tasks: {percent_incomp_overdue_per_user[u_print]}\n'
            user_report.write(u_str)
    

#########################
# Main Program
######################### 

while True:
    # Get input from user
    print()
    if curr_user == 'admin':
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    ds - display statistics
    gr - generate reports
    e - Exit
    : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()

    if menu == 'r': # Register new user (if admin)
        if curr_user != 'admin':
            print("Registering new users requires admin privileges")
        else:
    #Request input of new user name
            new_username = input("New Username: ")
    # Request input of a new password
            new_password = input("New Password: ")
            reg_user(new_username,new_password)

    elif menu == 'a': # Add a new task
        # Prompt a user for the following: 
        #     A username of the person whom the task is assigned to,
        #     A title of a task,
        #     A description of the task and 
        #     the due date of the task.
             # Ask for username
        task_username = input("Name of person assigned to task: ")
        add_task(task_username)

    elif menu == 'va': # View all tasks
        view_all()

    elif menu == 'vm': # View my tasks
        view_mine()


    elif menu == 'ds' and curr_user == 'admin': # If admin, display statistics
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")

    elif menu == 'e': # Exit program
        print('Goodbye!!!')
        exit()

    elif menu == 'gr' and curr_user == 'admin':
        #tasks overview 
        task_overview()
        user_overview()
        print('Report Generated!!')

    else: # Default case
        print("You have made a wrong choice, Please Try again")