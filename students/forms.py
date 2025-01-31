from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  
        exclude = ['student_id']


class StudentFormALL(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'  