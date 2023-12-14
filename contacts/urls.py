from django.urls import path

from .views import ContactListView,ContactCreateView,ContactDetailView

urlpatterns = [
    path("", ContactListView.as_view(), name="contact_list"),
    path("create/", ContactCreateView, name="contact_create"),
    path("contacts/<int:pk>/", ContactDetailView.as_view(), name="contact_detail"),

]