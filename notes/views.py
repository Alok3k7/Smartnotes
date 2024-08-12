from typing import Any, List
from django.http.response import HttpResponseRedirect
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/templates/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    template_name = 'notes/templates/notes_form.html'

class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
    template_name = 'notes/templates/notes_form.html'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/templates/notes_list.html'
    login_url = '/admin'
    
    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/templates/notes_detail.html'
