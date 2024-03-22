from django.urls import path
from lojaderoupas import views

urlpatterns = [
    path('',views.index,name='index'),
    
]
