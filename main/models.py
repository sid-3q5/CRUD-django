from django.db import models

# Create your models here.
class List(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    program = models.CharField(max_length=100)
    status2 = models.CharField(max_length=9, choices= [("Married","Married"), ("Unmarried","Unmarried")], null=True)
    country = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['pk']
    # title = models.CharField(max_length = 200)
    # description = models.TextField()
 
    # renames the instances of the model
    # # with their title name
    # def __str__(self):
    #     return self.title
