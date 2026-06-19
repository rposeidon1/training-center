from django.urls import path
from core import api_views

urlpatterns = [
    path("students/", api_views.StudentListAPIView.as_view(), name="api_student_list"),
    path("student/<int:pk>/", api_views.StudentDetailView.as_view(), name="api_student_detail"),
    path("course/", api_views.CourseListAPIView.as_view(), name="api_course_list"),
    path("course/<int:pk>/", api_views.CourseDetailView.as_view(), name="api_course_detail"),
]

