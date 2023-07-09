from django.shortcuts import render
from django.http import HttpResponse
import os
import json
file_path = os.path.join(os.path.dirname(__file__),'places.json')
with open(file_path,"r") as file:
    data = json.load(file)


def listing(request):
    return render(request, "list.html", {"data":data})

# Create your views here.
