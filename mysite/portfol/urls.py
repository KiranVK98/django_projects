from django.urls import path, reverse_lazy
from .views import PortListView, PortProjectView, PortContactView, PortSkillsView, PortEducationView


app_name='port'

urlpatterns=[
    path('', PortListView, name='about_me'),
    path('project', PortProjectView, name='projects'),
    path('contact', PortContactView, name='contact'),
    path('skills', PortSkillsView, name='skills'),
    path('education', PortEducationView, name='education'),
]

