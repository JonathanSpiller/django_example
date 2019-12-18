from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    return render(request, "phonebook/index.html")


def home(request, number=0):
    return render(request, "phonebook/home.html")


def persons(request):

    person_list = models.Person.objects.all().order_by('last_name')

    person_list_dict = {
        'persons': person_list
    }

    return render(request, "phonebook/person_list.html", person_list_dict)


def person(request, id):
    person = models.Person.objects.get(id=id)
    return render(request, "phonebook/person_detail.html", {'person':person})