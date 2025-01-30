from django.urls import path, include
from . import views
from .views import check_id 

urlpatterns = [
    path("addstudent", views.addstudent , name="addstudent"),
    path("deletestudent", views.deletestudent, name="deletestudent"),
    path("departmentassignment", views.departmentAssignment , name="departmentassignment"),
    path("search", views.search , name="search"),
    path('search/', views.search_page, name='search_page'), 

    path("udatehome", views.updatehome , name="updatehome"),

    # because when in updatehome page there each student has a botton that 
    # when i click on it it moves me to the update page, and edit that student information.
    path('updateinfo/<int:student_id>/', views.updateinfo, name='updateinfo'),
    path("view", views.view , name="view"),
    # paths of the functions
    path('check-id/', views.check_id, name='check_id'),
    path('deleterecord/<int:record_id>/', views.delete_record, name='delete_record'),
    # path to function that changes the status of student 
    path('change_status/<int:student_id>/', views.change_status, name='change_status'),
    path('edit_all_student_information/<int:student_id>/', views.edit_all_student_information, name='edit_all_student_information'),
]