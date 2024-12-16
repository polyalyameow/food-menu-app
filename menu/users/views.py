from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            messages.success(request, f"""
                             Welcome {username}! Your account is created
                             """)
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})


def logout_view(request):
    logout(request)

    return render(request, "users/logout.html")


@login_required
def profilepage(request):
    return render(request, "users/profile.html")
