from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util


def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def generate(request,title):

    titleU = title.upper()
    titleC = title.capitalize()
    contentU = util.get_entry(titleU)
    contentC = util.get_entry(titleC)

    if titleU == "CSS" or titleU == "HTML":
        return render(request,f"encyclopedia/{titleU}.html",{
            "content": contentU
        })
    else:
        if contentC == None:
            return render(request, f"encyclopedia/error.html")
        return render(request, f"encyclopedia/{titleU}.html",{
            "content": contentC
        })
        




 