from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


def forbidden_user(value):
    forbidden_users = ['login', 'logout', 'django', 'python']

    if value.lower() in forbidden_users:
        raise ValidationError('Choose some other name, this enlisted for special function')


def invalid_id(value):
    if '@' in value or '+' in value or '!' in value:
        raise ValidationError('dont use these sintaxes')


def unique_mail(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError('there is already a user registered with this email')


def unique_user(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError('username exist')


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(), required=True)
    email = forms.CharField(max_length=100, widget=forms.EmailInput(), required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True, label='confirm your password')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(forbidden_user)
        self.fields['username'].validators.append(invalid_id)
        self.fields['username'].validators.append(unique_user)
        self.fields['email'].validators.append(unique_mail)

    def clean(self):
        super(SignupForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            self._errors['password'] = self.error_class(['password does not match'])
        return self.cleaned_data