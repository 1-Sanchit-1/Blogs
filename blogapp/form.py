from django import forms

class InputForm(forms.Form): 
    first_name = forms.CharField(max_length = 200) 
    last_name = forms.CharField(max_length = 200) 
    email = forms.EmailField() 
    subject=forms.CharField(max_length=1000) 
    Message=forms.CharField(max_length=5000) 

    


