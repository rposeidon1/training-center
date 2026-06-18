from django.contrib import admin

from core.models import Course, Enrollment, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "created_at","updated_at"]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "duration", "created_at", "updated_at"]

@admin.register(Enrollment)
class Enrollment(admin.ModelAdmin):
    list_display = ["student", "course", "enrolled_at"]