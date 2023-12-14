from django.shortcuts import render
from django.views.generic import ListView

from .models import Contact

# Create your views here.
class ContactListView(ListView):
    model = Contact
