from django.shortcuts import redirect, render
from .models import Board, Reply

from django.core.paginator import Paginator
# Create your views here.

def index(request):
    b = Board.objects.all()
    page = request.GET.get("page", 1)
    pag = Paginator(b, 10)
    obj = pag.get_page(page)
    context = {
        'con' : obj
    }
    return render(request, "board/index.html", context)

def detail(request, num):
    try:
        b = Board.objects.get(id=num)
        r = b.reply_set.all()
        pag = Paginator(r, 3)
        obj = pag.get_page(1)
        context = {
            'con' : b,
            'rep' : obj,
        }
    except:
        return render(request, "error/notfound.html")
    return render(request, "board/detail.html", context)

def create(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        writer = request.user.username
        content = request.POST.get("content")
        Board(subject=subject, writer=writer, content=content, likey=0).save()
        return redirect('board:index')

    return render(request, "board/create.html")

def delete(request, conid):
    try:
        b = Board.objects.get(id=conid)
        if b.writer == request.user.username:
            b.delete()
        else:
            return render(request, "error/forbidden.html")
    except:
        return render(request, "error/notfound.html")
    return redirect('board:index')

def update(request, conid):
    b = Board.objects.get(id=conid)
    if request.user.username == b.writer:
        if request.method == "POST":
            b.subject = request.POST.get("subject")
            b.content = request.POST.get("content")
            b.save()
            return redirect("board:detail", num=conid)
        context = {
            'con' : b
        }
        return render(request, "board/update.html", context)
    else:
        return render(request, "error/forbidden.html")

def create_reply(request, conid):
    b = Board.objects.get(id=conid)
    r = request.user.username
    c = request.POST.get('comment')
    p = request.user.userpic
    Reply(subject=b, replyer=r, comment=c, pic=p).save()
    return redirect('board:detail', num=conid)

def delete_reply(request, conid, num):
    Reply.objects.get(id=num).delete()
    return redirect('board:detail', num=conid)

def vote(request, conid):
    b = Board.objects.get(id=conid)
    if request.user in b.up.all():
        b.up.remove(request.user)
    else:
        b.up.add(request.user)
    b.save()
    return redirect("board:detail", num=conid)