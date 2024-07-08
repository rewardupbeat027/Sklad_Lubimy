from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Employee(models.Model):
    name1 = models.CharField('Имя', max_length=100)
    name2 = models.CharField('Фамилия', max_length=100)
    status = models.CharField('Должность', max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employee_account')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_employees',
                                   verbose_name="Зарегистрирован Главой")

    def __str__(self):
        return f'{self.name1} {self.name2}'


class Category(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    category = models.CharField('Категория', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registration_category')
    name1 = models.ForeignKey(Employee, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.category


class Inventar(models.Model):
    name = models.CharField('Название', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_category')
    kod = models.IntegerField('Код')
    price = models.FloatField('Цена')
    image = models.ImageField(upload_to='images/', blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registration_inventar')

    def __str__(self):
        return self.name

class Images(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)

class Profile(models.Model):
    main = models.CharField(max_length=100)
    disc = models.CharField(max_length=100)
    text = models.CharField(max_length=250)
    imag = models.ForeignKey(Images, on_delete=models.CASCADE, related_name='imageernkol')





