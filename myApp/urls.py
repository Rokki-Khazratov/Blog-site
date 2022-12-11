from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('news/',views.news,name = 'news'),
    path('single/',views.single,name = 'single')
]