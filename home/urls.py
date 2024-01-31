from django.urls import path
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.about, name='about'),
    path('programs', views.program, name='program'),
    path('blog', views.blog, name='blog'),
    path('event', views.event, name='event'),
    path('contact', views.contact, name='contact'),
]

