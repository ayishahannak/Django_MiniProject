from django.http import HttpResponse
from django.shortcuts import render

from newApp.form import foodForm
from newApp.models import menu


# Create your views here.
def home(request):
    return HttpResponse("Hello Worldd")

def index(request):
    return render(request,"index.html")

def dashboard(request):
    return render(request,"dashboard.html")
def food_data(request):
    form=foodForm()

    if request.method=="POST":
        form_data=foodForm(request.POST)
        if form_data.is_valid():
            form_data.save()
    return render(request,"foodForm.html",{"form":form})

def menu_view(request):
    data = menu.objects.all()
    # print(data)

    return render(request,"menu_view.html",{"data":data})