from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^about/',views.about,name = 'about'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^$', views.CourseListView.as_view(), name='course_list'),
    # url(r'^module/(?P<module_id>\d+)/$', views.ModuleContentListView.as_view(), name='module_content_list'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)