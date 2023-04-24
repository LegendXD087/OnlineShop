from django.shortcuts import render, redirect
from .forms import AddUserForm
from .models import AddUser

details = AddUser.objects.all()


def index(request):
    error = ''
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form Invalid'
    form = AddUserForm()
    context = {
        "form": form,
        "error": error,
        "details": details
    }
    return render(request, "index.html", context)


def home(request):
    detail = AddUser.objects.order_by("-id")[:1]
    form = AddUserForm()
    context = {
        "form": form,
        "pro": detail
    }
    return render(request, "home.html", context)
