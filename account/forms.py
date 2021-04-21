from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        self.fields['username'].label = "User Name"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'Enter User Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
    class Meta:

        model=User

        fields = ['email','username', 'password1', 'password2',]


    def save(self, commit=True):
        user = UserCreationForm.save(self,commit=False)
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email =  forms.EmailField(
    widget=forms.EmailInput(attrs={ 'placeholder':'Email',})
) 
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={
        
        'placeholder':'Password',
    }))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("User Does Not Exist.")

            if not user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")

            if not user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user



# class EmployeeProfileEditForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super(EmployeeProfileEditForm, self).__init__(*args, **kwargs)
#         self.fields['first_name'].widget.attrs.update(
#             {
#                 'placeholder': 'Enter First Name',
#             }
#         )
#         self.fields['last_name'].widget.attrs.update(
#             {
#                 'placeholder': 'Enter Last Name',
#             }
#         )

#     class Meta:
#         model = User
#         fields = ["first_name", "last_name", "gender"]
