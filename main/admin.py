from django.contrib import admin
from .models import Employee, Inventar, Category, Images, Profile

admin.site.register(Employee)
admin.site.register(Inventar)
admin.site.register(Category)
admin.site.register(Images)
admin.site.register(Profile)