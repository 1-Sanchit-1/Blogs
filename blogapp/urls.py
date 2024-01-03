from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index , name='index'), 
     path('registration_page' ,views.registration_page, name='registration_page'),
    path('category/<slug:url>',views.category , name='category'), 
    path('blog/<slug:url>' ,views.post,name='post'),
]
