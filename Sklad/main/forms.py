from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django_recaptcha.fields import ReCaptchaField

from .models import Inventar, Employee, Category


class InventarForm(ModelForm):
    class Meta:
        model = Inventar
        fields = '__all__'
        exclude = ['slug', 'user', 'created_at', 'updated_at', ]


from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import Employee

class EmployeeForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    email = forms.EmailField(label='Электронная почта')
    group = forms.ModelChoiceField(queryset=Group.objects.exclude(name='Глава'), label='Группа')

    class Meta:
        model = Employee
        fields = ('name1', 'name2', 'status', 'username', 'password', 'email', 'group')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EmployeeForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        user.groups.add(self.cleaned_data['group'])
        user.save()
        employee = super(EmployeeForm, self).save(commit=False)
        employee.user = self.user
        employee.created_by = user
        if commit:
            employee.save()
        return employee



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ['user',]