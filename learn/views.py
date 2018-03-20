from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http  import HttpResponse

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return HttpResponse('Welcome to the Online-learning')
