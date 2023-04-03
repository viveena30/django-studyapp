from django.contrib import admin
from .models import *
# from .models import Notes, Homework, Todo

class NotesAdmin(admin.ModelAdmin):
    list_display = ['user','title','description']
    search_fields = ['user','title','description' ]

class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ['user','title','subject','description', 'due', 'is_finished' ]
    search_fields = ['user','title','subject','description', 'due', 'is_finished' ]

class ToDoAdmin(admin.ModelAdmin):
    list_display = ['user','title','description','is_finished' ]
    search_fields = ['user','title','description','is_finished' ]


admin.site.register(Notes, NotesAdmin)
admin.site.register(Homework,HomeWorkAdmin)
admin.site.register(Todo, ToDoAdmin)