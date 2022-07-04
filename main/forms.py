from django import forms
from .models import List

# creating a form
class Student(forms.ModelForm):
    CHOICES = [("Married","Married"), ("Unmarried","Unmarried")]

    student_id = forms.IntegerField(label="Student ID ")
    first_name = forms.CharField(max_length=100, label="Student First Name ")
    last_name = forms.CharField(max_length=100, label="Student Last Name ")
    address = forms.CharField(max_length=200,label="Student Address ")
    program = forms.CharField(max_length=100, label="Student Program ")
    status2 = forms.CharField(label='Student Martial Status ', widget=forms.RadioSelect(choices=CHOICES))
    country = forms.CharField(max_length=30,label='Country ')

    class Meta:
        model = List
        # fields = [
        #     "title",
        #     "description",
        # ]
        fields = ['student_id', 
                    'first_name', 
                    'last_name', 
                    'address', 
                    'program', 
                    'status2', 
                    'country']