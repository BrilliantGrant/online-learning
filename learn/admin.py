from django.contrib import admin
from .models import Course, Category,Subject,Post

# Register your models here.

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(Post)



