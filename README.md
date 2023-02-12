# finalCapstone
Projects completed using the skills gained from the HyperionDev Data Science bootcamp

TASK 7
For this task, assume that you have been approached by a small financial
company and asked to create a program that allows the user to access two
different financial calculators: an investment calculator and a home loan
repayment calculator.


TASK 21
You will notice that the main body of the code requires functionality for
registering a user, adding a task, viewing all tasks and viewing the current
user's tasks. However, because there is so much functionality needed to
complete this, the main body of the loop becomes difficult to read. Using
the principle of abstraction, refactor the code to create and use the
following functions:
o reg_user — that is called when the user selects ‘r’ to register a user.
o add_task — that is called when a user selects ‘a’ to add a new task.
o view_all — that is called when users type ‘va’ to view all the tasks
listed in ‘tasks.txt’.

view_mine — that is called when users type ‘vm’ to view all the
tasks that have been assigned to them.

Modify the function called reg_user to make sure that you don’t duplicate
usernames when you add a new user to user.txt. If a user tries to add a
username that already exists in user.txt, provide a relevant error message
and allow them to try to add a user with a different username.
● functionality when the user selects ‘vm’ to view all the
tasks assigned to them:
o Display all tasks in a manner that is easy to read. Make sure that
each task is displayed with a corresponding number which can be
used to identify the task.
o Allow the user to select either a specific task (by entering a number)
or input ‘-1’ to return to the main menu.
o If the user selects a specific task, they should be able to choose to
either mark the task as complete or edit the task. If the user
chooses to mark a task as complete, the ‘Yes’/’No’ value that
describes whether the task has been completed or not should be
changed to ‘Yes’. When the user chooses to edit a task, the
username of the person to whom the task is assigned or the due
date of the task can be edited. The task can only be edited if it has
not yet been completed.
● Add an option to generate reports to the main menu of the application
Compulsory Task 1
● Use the task_manager.py file for this project. Also, make use of the
supporting text files (user.txt and tasks.txt) that accompany this
Capstone project in this folder. In this task you will be modifying this
program.
● You will notice that the main body of the code requires functionality for
registering a user, adding a task, viewing all tasks and viewing the current
user's tasks. However, because there is so much functionality needed to
complete this, the main body of the loop becomes difficult to read. Using
the principle of abstraction, refactor the code to create and use the
following functions:
o reg_user — that is called when the user selects ‘r’ to register a user.
o add_task — that is called when a user selects ‘a’ to add a new task.
o view_all — that is called when users type ‘va’ to view all the tasks
listed in ‘tasks.txt’.
o view_mine — that is called when users type ‘vm’ to view all the
tasks that have been assigned to them.
● Modify the function called reg_user to make sure that you don’t duplicate
usernames when you add a new user to user.txt. If a user tries to add a
username that already exists in user.txt, provide a relevant error message
and allow them to try to add a user with a different username.
● Add the following functionality when the user selects ‘vm’ to view all the
tasks assigned to them:
o Display all tasks in a manner that is easy to read. Make sure that
each task is displayed with a corresponding number which can be
used to identify the task.
o Allow the user to select either a specific task (by entering a number)
or input ‘-1’ to return to the main menu.
o If the user selects a specific task, they should be able to choose to
either mark the task as complete or edit the task. If the user
chooses to mark a task as complete, the ‘Yes’/’No’ value that
describes whether the task has been completed or not should be
changed to ‘Yes’. When the user chooses to edit a task, the
username of the person to whom the task is assigned or the due
date of the task can be edited. The task can only be edited if it has
not yet been completed.
● Add an option to generate reports to the main menu of the application
 When the user chooses to generate reports, two text files, called
task_overview.txt and user_overview.txt, should be generated. Both
these text files should output data in a user-friendly, easy to read manner.
o task_overview.txt should contain:
▪ The total number of tasks that have been generated and
tracked using the task_manager.py.
▪ The total number of completed tasks.
▪ The total number of uncompleted tasks.
▪ The total number of tasks that haven’t been completed and
that are overdue.
▪ The percentage of tasks that are incomplete.
▪ The percentage of tasks that are overdue.
o user_overview.txt should contain:
▪ The total number of users registered with task_manager.py.
▪ The total number of tasks that have been generated and
tracked using task_manager.py.
▪ For each user also describe:
▪ The total number of tasks assigned to that user.
▪ The percentage of the total number of tasks that have
been assigned to that user
▪ The percentage of the tasks assigned to that user that
have been completed
▪ The percentage of the tasks assigned to that user that
must still be completed
▪ The percentage of the tasks assigned to that user that
have not yet been completed and are overdue


TASK 34
EDA on a movies and automobile dataset. To do this, I:
- Loaded the dataframe in
- Cleaned the data
- Removed duplicate rows
- Discarded entries with a zero movie budget
- Manipulated certain columns to the correct data type
- Answered questions about the data


TASK 36
EDA on a dataset containing  harmonized variables, including basic characteristics of individuals such as age, sex, marital status, disability status, literacy, education and work. It is at the individual level.

 To do this, I:
- Loaded the dataframe in
- Cleaned the data
- Removed duplicate rows
- Discarded entries with a zero movie budget
- Manipulated certain columns to the correct data type
- Answered questions about the data

TASK 39
Program that can be used by a bookstore clerk as a database for books in store. The program allows the clerk to:
○ add new books to the database
○ update book information
○ delete books from the database
○ search the database to find a specific book.


TASK 51
This dataset is from the US Arrests Kaggle challenge (link). A description of the
data is given as: “This data set contains statistics, in arrests per 100,000 residents,
for assault, murder, and rape in each of the 50 US states in 1973. Also given is the
percent of the population living in urban areas.”

● Use the dataset UsArrests.csv included in this folder to generate a similar
in-depth PCA report of the data. Explore as much as you can, motivate the
pre-processing steps you take, and interpret the outcomes of any analyses.
● You are also required to do an application of two clustering techniques and
an analysis of the clusters they generate. Try and see if you can find anything
common within each cluster that has been found.
