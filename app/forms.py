from django import forms   
from django.contrib.auth import authenticate, get_user_model
from django.http import request
from .models import Reservation

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email Adress')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')      
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('This email is already being used')  
        return email
            

class NewReservation(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'Offer', 
            'Barber', 
            'Date',
        ]

        def form_valid(self, form):
            form.instance.created_by = self.request.user
            return super().form_valid(form)