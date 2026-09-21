from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', context={'courses': courses})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course_detail.html', context={'course': course})


def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_create.html', context={'form': form, 'title': "Yangi kurs qo'shish"})

def course_update(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', id=course.id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_update.html', context={'form': form, 'title': "Kursni tahrirlash"})


def course_delete(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == "POST":
        course.delete()
        return redirect('course_list')
    return render(request, 'course_delete.html', context={'course': course})