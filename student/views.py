from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView,
    DetailView
)
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Student
from .forms import StudentForm


class StudentListView(ListView):
    queryset = Student.objects.all()
    model = Student
    template_name = 'student/list.html'
    context_object_name = 'students'


class StudentAddView(CreateView):
    model = Student
    template_name = 'student/add.html'
    form = StudentForm
    success_url = reverse_lazy('student-list')
    fields = ['name', 'date_of_birth']


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/detail.html'
    context_object_name = 'student'


class StudentActionView(DetailView):
    model = Student
    template_name = 'student/action.html'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()
        context['age'] = (timezone.now().date() - student.date_of_birth).days / 365
        return context


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/update.html'
    form = StudentForm
    success_url = reverse_lazy('student-list')
    fields = ['name', 'date_of_birth']
    context_object_name = 'student'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student-list')
    template_name = 'student/delete.html'
