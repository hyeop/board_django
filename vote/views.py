from django.shortcuts import render,redirect
from .models import Voter, Vote
# Create your views here.
def index(request):
    v = Voter.objects.all()
    context= {
        'con' : v
    }
    return render(request, "vote/index.html", context)

def create(request):
    
    if request.method == "POST":
        s = request.POST.get("subject")
        c = request.POST.get("comment")
        w = request.user.username
        topics = request.POST.getlist("topic")
        v = Voter(subject=s, comment=c, wrtier=w)
        v.save()
        for i in topics:
            Vote(subject=v, name=i).save()
        return redirect("vote:index")

    return render(request, "vote/create.html")

def detail(request, num):
    v = Voter.objects.get(id=num)
    if request.method == "POST":
        index = int(request.POST.get("3"))
        vo = v.vote_set.all()
        vo[index].num += 1
        vo[index].save()
    top = v.vote_set.all()
    context = {
        'con' : v,
        'topic' : top
    }
    return render(request, "vote/detail.html", context)