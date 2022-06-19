# from accounts.models import Profile
from photo.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError
            return cd['password2']


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = fields = ['username', 'first_name', 'last_name', 'email', 'gender', 'birthdate']
