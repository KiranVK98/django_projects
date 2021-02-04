from django.shortcuts import render
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
