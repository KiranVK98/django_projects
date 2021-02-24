from django.urls import path, reverse_lazy
from .views import PortListView, PortProjectView, PortContactView, PortSkillsView, PortEducationView
from . import views

app_name='port'

urlpatterns=[
    path('', PortListView, name='about_me'),
    path('project', PortProjectView, name='projects'),
    path('contact', PortContactView, name='contact'),
    path('skills', PortSkillsView, name='skills'),
    path('education', PortEducationView, name='education'),
    path('feedback', views.PortFeedbackView.as_view(), name='feedback'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(success_url=reverse_lazy('port:feedback')), name='port_comment_delete'),
]

