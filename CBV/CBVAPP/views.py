from django.shortcuts import render
from CBVAPP.models import Student
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
class StudentListView(ListView):
    model=Student
class StudentDetailView(DetailView):
    model=Student
class StudentCreateView(CreateView):
    model=Student
    fields="__all__"
class StudentDeleteView(DeleteView):
    model=Student
    success_url=reverse_lazy("student")
class StudentUpdateView(UpdateView):
    model=Student
    fields=("name","marks")


# Create your views here.
