from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import Contact
from .contact_form import ContactForm

from .models import Contact

# Create your views here.
class ContactListView(ListView):
    model = Contact

def ContactCreateView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # This will create a new Contact instance
            return redirect('contact_list')  # Redirect to the contact list page or any other page
    else:
        form = ContactForm()

    return render(request, 'contacts/contact_form.html', {'form': form})