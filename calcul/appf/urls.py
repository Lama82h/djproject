from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # Serve the index view
    path("taxrate",views.taxrate, name="taxrate"),
    path("anynumber/<int:number>/", views.anynumber, name="anynumber"),
]
