from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def index(request):
    return render(request, "index.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print(dir(request))
            return redirect("acc:index")
    return render(request, "acc/login.html")

def logout_user(request):
    logout(request)
    return redirect("acc:index")

def signup_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nickname = request.POST.get('nickname')
        comment = request.POST.get('comment')
        userpic = request.FILES.get('userpic')
        try:
            User.objects.create_user(username=username, password=password, nickname=nickname, comment=comment, userpic=userpic).save()
        except:
            print("계정있음")
        return redirect("acc:login_user")
    return render(request, "acc/signup.html")

def profile_user(request):
    return render(request, "acc/profile.html")
    
def update(request):
    user = request.user.username
    u = User.objects.get(username=user)
    if request.method == "POST":
        p = request.POST.get("password")
        if p:
            u.set_password(p)
        u.nickname = request.POST.get("nickname")
        u.comment = request.POST.get("comment")
        up = request.FILES.get('userpic')
        if up:
            u.userpic = up
        u.save()
        user_auth = authenticate(username=user, password=p)
        login(request, user_auth)
        return redirect("acc:profile_user")


    return render(request, "acc/update.html")

def delete(request):
    User.objects.get(username=request.user.username).delete()
    return redirect('acc:login_user')