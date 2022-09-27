from email.policy import default
from django.shortcuts import render

from . import util
from markdown2 import Markdown
import random

markdowner = Markdown()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def show(request,entry):
    
    entrychk = util.get_entry(entry)
    if entrychk is None:
        return render(request, "encyclopedia/entry_not_found.html", {
            "entry_title": entry
        })
    else:
        return render(request,"encyclopedia/entry.html",{
            "entry": markdowner.convert(entrychk),
            "entry_title": entry
        })

    
# def show(request,entry):
    
#     entrychk = util.get_entry(entry)
#     if entrychk is None:
#         return render(request, "encyclopedia/entry_not_found.html", {
#             "entry_title": entry
#         })
#     else:
#         return render(request,"encyclopedia/entry.html",{
#             "entry": markdowner.convert(entrychk),
#             "entry_title": entry
#         })


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title','default')
        content = request.POST.get('content','default')
        entries = util.list_entries()
        if title in entries:
            pass
        else:
            util.save_entry(title,content)
            path = util.get_entry(title)
            return render(request,"encyclopedia/entry.html",{
                "entry": markdowner.convert(path),
                "entry_title": title
            })
    
    return render(request, "encyclopedia/create.html")


def search(request):
    query = request.GET.get('q','default')
    print(query)
    entries = util.list_entries()
    possible=[]

    if (query in entries):
        path = util.get_entry(query)
        return render(request,"encyclopedia/entry.html",{
            "entry": markdowner.convert(path),
            "entry_title": query
        })

    else:
        for i in entries:
            if query in i:
                possible.append(i)
        return render(request,"encyclopedia/search.html",{
            "entries": possible
        })


def randm(request):
    entries = util.list_entries()
    rand_entry = random.choice(entries)
    print(rand_entry)
    entrychk = util.get_entry(rand_entry)

    return render(request,"encyclopedia/entry.html",{
        "entry": markdowner.convert(entrychk),
        "entry_title": rand_entry
    })


def edit(request):
    entry= request.POST.get('ed','default')
    path = util.get_entry(entry)
    return render(request, "encyclopedia/edit.html",{
        "entry_title" : entry,
        "para": path
    })
    

def save_edit(request):
    if request.method == 'POST':
        title = request.POST.get('title','default')
        content = request.POST.get('content','default')
        
        util.save_entry(title,content)
        path = util.get_entry(title)
        return render(request,"encyclopedia/entry.html",{
            "entry": markdowner.convert(path),
            "entry_title": title
        })