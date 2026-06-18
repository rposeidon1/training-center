from django.urls import path
from core import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("student-list/", views.StudentListView.as_view(), name="students"),
    path("student/<int:pk>/", views.StudentDetailView.as_view(), name="student"),
    path("student/create/", views.StudentCreateView.as_view(), name="create_student"),
    path("student/<int:pk>/update/", views.StudentUpdateView.as_view(), name="update_student"),
    path("student/<int:pk>/delete/", views.StudentDeleteView.as_view(), name="delete"),
    path("course-list/", views.CourseListView.as_view(), name="courses"),
    path("course/<int:pk>/", views.CourseDetailView.as_view(), name="course"),
    path("course/create/", views.CourseCreateView.as_view(), name="create_course"),
    path("course/<int:pk>/update", views.CourseUpdateView.as_view(), name="update_course"),
    path("course/<int:pk>/delete", views.CourseDeleteView.as_view(), name="delete"),
]