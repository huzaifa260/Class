from django.contrib import admin
from .models import Student, user, Receipt

# Register your models here.
admin.site.register(Student)
admin.site.register(user)
admin.site.register(Receipt)
