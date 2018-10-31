'''from django import forms
from homePage.models import User,Feedback

class formLogin(forms.ModelForm):
    class Meta():
        model = User
        fields=['EmailID','Password']

class formFeedback(forms.ModelForm):
    class Meta():
        model = Feedback
        fields='__all__'

'''






