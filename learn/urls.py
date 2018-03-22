from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import GeneratePDF

urlpatterns=[
    url(r'^post/',views.post,name = 'post'),
    url(r'^$',views.index,name = 'index'),
    url(r'^about/',views.about,name = 'about'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^$', views.CourseListView.as_view(), name='course_list'),
    url(r'^business/', views.business, name='business'),
    url(r'^language/', views.language, name='language'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^technology/', views.technology, name='technology'),
    url(r'^pdf/$',GeneratePDF.as_view(),name="generate"),
    url(r'^new/post$', views.new_post, name='new_post'),

    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)