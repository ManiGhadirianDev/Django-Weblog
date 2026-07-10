from django.urls import path
from firstOne.views import *

app_name='firstOne'


urlpatterns = [
   path('',index_view,name="index"),
   path('about',about_view,name="about"),
   path('contact',contact_view,name="contact"),
]