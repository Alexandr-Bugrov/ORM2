from django.contrib import admin

from .models import Student, Teacher

class StudentTeacher(admin.TabularInline):
    model = Student.teachers.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [
        StudentTeacher,
    ]
    exclude = ('teachers',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [
        StudentTeacher,
    ]
