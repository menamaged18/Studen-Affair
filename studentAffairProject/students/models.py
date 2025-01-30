from django.db import models

LEVEL_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
]

DEPARTMENT_CHOICES = [
    ('AI', 'AI'),
    ('CS', 'CS'),
    ('IT', 'IT'),
    ('IS', 'IS'),
    ('DS', 'DS'),
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

ACTIVE_CHOICES = [
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
]

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    email =  models.EmailField(max_length=254)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES) 
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES, null=True, blank=True) 
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES) 
    status = models.CharField(max_length=10, choices=ACTIVE_CHOICES) 

    # in the admin panel to change from: Student object (1) --> to: student_id or any thing in the module. 
    # def __str__(self):
    #     return self.student_id



