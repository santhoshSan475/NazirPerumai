from django import forms

class RegisterForm(forms.Form):
    FirstName = forms.CharField(max_length=200)
    LastName = forms.CharField(max_length=200)
    mobileNo = forms.CharField(max_length=200)
    EmailAddress = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    confirmPassword = forms.CharField(max_length=200)

class DemoForm(forms.Form):
    name = forms.CharField(min_length=15,max_length=200, label="firstName",)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput)
    date = forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    agree = forms.BooleanField(label="I agree the terms and conditions")
    gender = forms.ChoiceField(choices=[("female","Female"),("male","Male"),("others","Others")], widget=forms.RadioSelect)
    season = forms.ChoiceField(choices=[("summer","Summer"),("winter","Winter"),("monsoon","monsoon"),("autumn",'autumn')])
    course = forms.MultipleChoiceField(choices=[("summer","Summer"),("winter","Winter"),("monsoon","monsoon"),("autumn",'autumn')])
    image = forms.ImageField()
    files = forms.FileField()
    text = forms.CharField(widget=forms.Textarea)