from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact),
    path('gallery', views.gallery),
    path('news', views.news),
    path('faq', views.faq),
    path('about', views.about),
    path('myinfo',views.myinfo),
    path('', views.index)
]
