from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
import csv
from django.http import HttpResponse
from django.views import View
from core.mixins import StaffOnlyMixin


from core.models import Student, Course, Enrollment



class StudentCSVExportView(StaffOnlyMixin, View):

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students.csv"'

        writer = csv.writer(response)
        writer.writerow(['First Name', 'Last Name', 'Email', 'Phone', 'Created At'])

        for student in Student.objects.all():
            writer.writerow([
                student.first_name,
                student.last_name,
                student.email,
                student.phone,
                student.created_at.strftime('%Y-%m-%d'),
            ])

        return response
    
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
    paginate_by = 1

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if query:
            return Student.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )
        return Student.objects.all()
    
    def get_template_names(self):
        if self.request.headers.get("HX-Request"):
            return ["core/partials/student_list_partial.html"]
        return ["core/student_list.html"]

class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "core/student_detail.html"
    context_object_name = "student"

class StudentCreateView(StaffOnlyMixin, CreateView):
    model = Student
    fields = ["first_name", "last_name", "email", "phone"]
    template_name = "core/student_form.html"
    success_url = reverse_lazy("students")

class StudentUpdateView(StaffOnlyMixin, UpdateView):
    model = Student
    fields = ["first_name", "last_name", "email", "phone"]
    template_name = "core/student_form.html"
    success_url = reverse_lazy("students")

class StudentDeleteView(StaffOnlyMixin, DeleteView):
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

class CourseCreateView(StaffOnlyMixin, CreateView):
    model = Course
    fields = ["title", "description", "duration"]
    template_name = "core/course_form.html"
    success_url = reverse_lazy("courses")

class CourseUpdateView(StaffOnlyMixin, UpdateView):
    model = Course
    fields = ["title", "description", "duration"]
    template_name = "core/course_form.html"
    success_url = reverse_lazy("courses")

class CourseDeleteView(StaffOnlyMixin, DeleteView):
    model = Course
    template_name = "core/course_confirm_delete.html"
    success_url = reverse_lazy("courses")