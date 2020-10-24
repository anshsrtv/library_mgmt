from django.db import models
import datetime
class Student(models.Model):
    roll_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.name:
            return str(self.roll_no)+"-"+self.name
        else:
            return str(self.roll_no)

class Book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    isbn = models.CharField('ISBN', max_length=13, default='0000000000000')
    issued = models.BooleanField(default=False)
    issued_to = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.title