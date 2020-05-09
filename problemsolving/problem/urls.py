from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_problemlist, name="Problems list"),
]
