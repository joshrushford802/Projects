from django.shortcuts import render
from django.middleware import csrf
from django import forms
from markdown2 import Markdown
import random
from . import util


def converter(name):
    """Converts the markdown file for html integration"""
    md_file = util.get_entry(name)
    md_converter = Markdown()
    md_converted = md_converter.convert(md_file)

    return md_converted


def index(request):
    """Home page"""
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, name):
    """Render entry based on url"""
    md_file = converter(name)

    if util.get_entry(name) != None:
        return render(request, "encyclopedia/entry.html", {
            "entry": md_file,
            "header": name
        })
    else:
        return render(request, "encyclopedia/error.html")


def search_bar(request):
    """This is the functionality of the search bar"""
    if request.method == "POST":
        q = request.POST['q']
        try:
            md_converter = converter(q)
            return render(request, "encyclopedia/entry.html", {
                "entry": md_converter,
                "header": q
            })
        except:
            entry_list = util.list_entries()
            i = 0
            matches = []

            while i < len(entry_list):
                if q in entry_list[i]:
                    matches.append(entry_list[i])
                i += 1

            if len(matches) == 0 or len(q) < 1:
                return render(request, "encyclopedia/error.html")
            else:
                return render(request, "encyclopedia/matching.html", {
                    "entries": matches
                })

    else:
            return render(request, "encyclopedia/error.html")


def add_new_entry(request):
    """Allows user to add a new entry"""
    if request.method == "POST":
        new_title = request.POST["new_title"]
        new_md = request.POST["new_md"]
        if util.get_entry(new_title) == None:
            util.save_entry(new_title, new_md)
            return render(request, "encyclopedia/entry.html", {
                "header": new_title,
                "entry": converter(new_title)
            })
        else:
            return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/add_new.html")


def edit_page(request):
    if request.method == "POST":
        title_edit = request.POST["title_edit"]
        return render(request, "encyclopedia/edit_page.html", {
            "title_edit": title_edit,
            "md_to_edit": util.get_entry(title_edit)
        })


def update_changes(request):
    if request.method == "POST":
        new_title = request.POST["updated_title"]
        new_md = request.POST["updated_md"]
        util.save_entry(new_title, new_md)
        return render(request, "encyclopedia/entry.html", {
            "header": new_title,
            "entry": converter(new_title)
        })
    else:
        return render(request, "encyclopedia/error.html")


def random_entry(request):
    if request.method == "GET":
        random_item = random.choice(util.list_entries())
        md_file = converter(random_item)
        return render(request, "encyclopedia/entry.html", {
            "entry": md_file,
            "name": random_item
        })
    else:
        return render(request, "encyclopedia/error.html")

