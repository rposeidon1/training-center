from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Student, Course, Enrollment

    
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()
        context["total_courses"] = Course.objects.count()
        context["total_enrollments"] = Enrollment.objects.count()
        return context