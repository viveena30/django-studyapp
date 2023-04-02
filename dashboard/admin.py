from django.contrib import admin
from .models import *
# from .models import Notes, Homework, Todo

admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)