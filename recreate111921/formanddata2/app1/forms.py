from django import forms
from .models import CommentData
#class CommentDataForm(forms.Form):
#    formname = forms.CharField(label="Your Name", required=True, max_length=30)
#    formemail = forms.CharField(label="Your Email Address", required=True, max_length=50)
#    formcomment = forms.CharField(label="Your Comment", widget=forms.Textarea, required=True, max_length=500)

class CommentDataForm(forms.ModelForm):
    class Meta:
        model = CommentData
        fields = '__all__'
        labels = {
            "name": "YOUR NAME",
            "email": "YOUR EMAIL",
            "comment": "YOUR COMMENT"
        }
        error_messages = {
            "name": {
              "required": "Your name must not be empty!",
              "max_length": "Please enter a shorter name!"
            }
        }
