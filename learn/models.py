from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created')
    # subject = models.ForeignKey(Subject, related_name='courses')
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(User, related_name='courses_joined', blank=True)
    upgraded = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length = 100)
    course = models.ForeignKey('Category', related_name='modules',default=1)
    pic = models.ImageField(upload_to = "pics/",null = True)

    class Meta:
        ordering = ('-created',)



    @classmethod
    def search_by_category(cls, search_term):
    	category = cls.objects.filter(course__title__icontains=search_term)
    	return category



    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category_name = models.CharField(max_length=30)
    pic = models.ImageField(upload_to = "pics/",null = True)


    def __str__(self):
    	return self.category_name


    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()