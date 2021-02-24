from django.shortcuts import render,redirect
from ads.owner import OwnerDeleteView,OwnerListView
from portfol.models import Feedback
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy,reverse
from portfol.forms import CommentForm
from django.contrib.humanize.templatetags.humanize import naturaltime
# Create your views here.


def PortListView(request):
    return render(request,'portfol/about.html')


def PortProjectView(request):
    return render(request,'portfol/project.html')

def PortContactView(request):
    return render(request,'portfol/contact.html')

def PortSkillsView(request):
    return render(request,'portfol/skills.html')

def PortEducationView(request):
    return render(request,'portfol/education.html')

class PortFeedbackView(LoginRequiredMixin, View):
    model=Feedback
    template_name="portfol/feedback.html"
    def get(self,request):
        x=Feedback.objects.filter().order_by('updated_at')
        comment_form=CommentForm()
        context={'comment':x,'comment_form':comment_form}
        return render(request,self.template_name,context)

    def post(self, request):
        comment=Feedback(text=request.POST['comment'],owner=request.user)
        comment.save()
        return redirect(reverse('port:feedback'))

class CommentDeleteView(OwnerDeleteView):
    model = Feedback
    template_name = "portfol/comment_delete.html"


