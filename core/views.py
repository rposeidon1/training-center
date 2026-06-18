from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from core.models import Student, Course, Enrollment

    
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()
        context["total_courses"] = Course.objects.count()
        context["total_enrollments"] = Enrollment.objects.count()
        return context
    
class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "core/student_list.html"
    context_object_name = "students"

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "core/student_detail.html"
    context_object_name = "student"

class StudentCreateView(CreateView):
    model = Student
    fields = ["first_name", "last_name", "email", "phone"]
    template_name = "core/student_form.html"
    success_url = reverse_lazy("students")

class StudentUpdateView(UpdateView):
    model = Student
    fields = ["first_name", "last_name", "email", "phone"]
    template_name = "core/student_form.html"
    success_url = reverse_lazy("students")

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "core/student_confirm_delete.html"
    success_url = reverse_lazy("students")






    
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "core/course_list.html"
    context_object_name = "courses"

class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "core/course_detail.html"
    context_object_name = "course"

class CourseCreateView(CreateView):
    model = Course
    fields = ["title", "description", "duration"]
    template_name = "core/course_form.html"
    success_url = reverse_lazy("courses")

class CourseUpdateView(UpdateView):
    model = Course
    fields = ["title", "description", "duration"]
    template_name = "core/course_form.html"
    success_url = reverse_lazy("courses")

class CourseDeleteView(DeleteView):
    model = Course
    template_name = "core/course_confirm_delete.html"
    success_url = reverse_lazy("courses")