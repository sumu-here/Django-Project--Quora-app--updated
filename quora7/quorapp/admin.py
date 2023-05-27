from django.contrib import admin
from .models import Question,Answers

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=('title','author')
    search_fields=('title','detail')
    
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answers)
