# Studen-Affair
## Student Affair is a Django web project where it has:
1. login/signup for employees and there is a superuser(manger) which he can access the database unlike normal users
2. add student page where employees can add student to the database
3. delete page where employees can delete students from the database
4. search page in where employees can search for a certain student by: id, name, level, gpa, department and after the search he can update information for a specific student
5. view page where employees can view student and change student status
 
## To make the project work
### First method
1. download the zip file
2. activate the virtual environment 
     --> to activate the virtual environment
        1. navigate to the virtual environment folder i.e(where Scripts, lib and studentAffairProject folders exist)
        2. type cd Scripts/activate
3. after activating the virtual environment navigate to studentAffairProject project i.e(where manage.py file exists)
4. type manage.py runserver and the server will be activated

### Second method
1. download the studentAffairProject folder
2. add it to virtual environment
3. then do the same steps after activating the virtual environment that in the first step
note: 
#### if needed in both steps:
1. navigate to studentAffairProject project i.e(where manage.py file exists)
2. type: python manage.py makemigrations
3. then: python manage.py migrate
