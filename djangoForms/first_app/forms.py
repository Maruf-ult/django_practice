from django import forms
from django.core import validators

#widgets == feild to html input 
class contactForm(forms.Form):
     name = forms.CharField(label="Full Name : ", initial="Rahim", help_text="Total length within 70 char", required=False, disabled=False, widget=forms.Textarea(attrs = {'id' : 'text_area', 'class' : 'class1 class2', 'placeholder' : 'Enter your name' }))
     file = forms.FileField()
     email = forms.EmailField(label= "User Email")
     age = forms.IntegerField()
     weight = forms.FloatField(widget=forms.NumberInput)
     balance = forms.DecimalField()
     check = forms.BooleanField()
     birthday = forms.CharField(widget=forms.DateInput( attrs= {'type' : 'date'}))
     appointment = forms.CharField(widget=forms.DateInput( attrs= {'type' : 'datetime-local'}))
     CHOICES = [('s', 'small'), ('M', 'Medium'), ('L', 'Large')]
     size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
     MEAL = [('p', 'pepperoni'), ('M', 'Mashroom'), ('B', 'Beef')]
     pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#      name = forms.CharField(widget=forms.TextInput)
#      email = forms.CharField(widget=forms.EmailInput)
#      # def clean_name(self):
#      #      valname = self.cleaned_data['name']
#      #      if len(valname) < 10:
#      #            raise forms.ValidationError("Enter a name with at least 10 characters")
#      #      return valname
     
#      # def clean_email(self):
#      #      valemail = self.cleaned_data['email']
#      #      if '.com' not in valemail:
#      #           raise forms.ValidationError("your email must contain .com")
#      #      return valemail
     
#      def clean(self):
#           cleaned_data = super().clean()
#           valname = self.cleaned_data['name']
#           valemail = self.cleaned_data['email']
#           if len(valname) < 10:
#                   raise forms.ValidationError("Enter a name with at least 10 characters")
       
#           if '.com' not in valemail:
#                raise forms.ValidationError("your email must contain .com")
     
def len_check(value):
      if len(value) < 10:
            raise forms.ValidationError("Enter a value at lest 10 chars")


class StudentData(forms.Form):
       name = forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter a name at least 10 char')])
       text = forms.CharField(widget=forms.TextInput,validators=[len_check])
       email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email")] )
       age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="Age must be maximum 34"), validators.MinValueValidator(24, message= "age must be at least 24"  )])
       file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message="File extension must  be ended with .pdf")])

from django import forms
from django.core import validators

class Authentication(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput, 
        validators=[validators.EmailValidator(message="Enter a valid email")]
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[validators.MinLengthValidator(5, message='Enter at least 5 characters')]
    )
    confirmPassword = forms.CharField(
        widget=forms.PasswordInput,
        validators=[validators.MinLengthValidator(5, message='Enter at least 5 characters')]
    )

    def clean_confirmPassword(self):
        
        cleaned_data = super().clean()

        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirmPassword']

        if val_conpass != val_pass:
             raise forms.ValidationError("password doesnot match")
        