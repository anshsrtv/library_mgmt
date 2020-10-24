from django import forms
from .models import Student, Book

class StudentForm(forms.ModelForm):
  class Meta:
       model = Student
       fields = ('roll_no', 'name', 'contact','address')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'isbn')
      
class IssueForm(forms.ModelForm):
  class Meta:
    model=Book
    fields = ('issued_to',)  
    
  def __init__(self, *args, **kwargs):
    super(IssueForm, self).__init__(*args, **kwargs)
    self.fields['issued_to'].required = True 