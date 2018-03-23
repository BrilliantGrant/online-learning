from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import contenttypes
from .models import Course, Subject,Category,Post
from django.views.generic.base import TemplateResponseMixin,View
import datetime
# from django.template import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf 
from . forms import PostForm




# Create your views here.

from django.http  import HttpResponse

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    title = 'E-learning'
    return render(request, 'index.html', {"title":title})

class CourseListView(TemplateResponseMixin, View):
    model = Course
    template_name = 'list.html'

    def get(self, request, subject=None):
        subjects = Subject.objects.annotate(total_courses=Count('courses'))
        courses = Course.objects.annotate(total_modules=Count('modules'))

        if subject:
            subject = get_object_or_404(Subject, slug=subject)
            courses = courses.filter(subject=subject)
        
        return self.render_to_response({'subjects': subjects, 'subject': subject, 'courses': courses })


@login_required(login_url='/accounts/login/')
def about(request):
      title = 'learning'
      
      return render(request, 'about.html', {"title":title})



@login_required(login_url='/accounts/login/')
def business(request):
      title = 'Business'
      
      return render(request, 'all/business.html', {"title":title})

@login_required(login_url='/accounts/login/')
def language(request):
      title = 'Language'
      
      return render(request, 'all/language.html', {"title":title})

@login_required(login_url='/accounts/login/')
def technology(request):
      title = 'Tech'
      
      return render(request, 'all/technology.html', {"title":title})

@login_required(login_url='/accounts/login/')
def contact(request):
      title = 'Contact'
      
      return render(request, 'all/contact.html', {"title":title})



def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Course.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search_category.html',{"message":message,"courses": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_category.html',{"message":message})


class GeneratePDF(View):
     def get(self, request, *args, **kwargs):
         data = {
              'today': datetime.date.today(),
              'amount': 39.99,
             'customer_name': 'Cooper Mann',
             'order_id': 1233434,
         }
         html = template.render(context)
         pdf = render_to_pdf('pdf/invoice.html', data)
         return HttpResponse(pdf, content_type='application/pdf')



@login_required(login_url='/accounts/login/')
def post(request):
    post = Post()
    return render(request,'post.html')



@login_required(login_url='/accounts/login/')
def new_post(request):

    current_user = request.user
    image_post = Post.objects.all()
    print(image_post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('new_post') 
    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form,"image_post":image_post})
