import requests
from django.shortcuts import render, redirect
from server.models import *
from server.forms import *

url = "https://api.telegram.org/bot5346235377:AAGg1mWc4FPRxGn1GFcnOBcj75MMLlrAJlA/sendMessage"


def index(request):
    meetings = Meeting.objects.all()
    questions = Question.objects.filter(Course=None)
    form_meet = ApplicationMeetForm
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            das = form.save(commit=False)
            payload = {
                "text": f"Гость оставил заявку на обратную связь\nЕго зовут {das.name}\nНомер телефона {das.phone}",
                "chat_id": '-1001519795077',
            }

            response = requests.post(url, json=payload)
            form.save()
            return redirect('/')
    return render(request, 'index.html', {'questions': questions, 'form': FeedbackForm, 'courses': Course.objects.all(), 'meetings': meetings, 'form_meet': form_meet})


def course_detail(request, pk):
    course = Course.objects.get(id=pk)
    questions = Question.objects.filter(Course=pk)
    if request.method == 'POST':
        form = ApplicationCourseForm(request.POST)
        das = form.save(commit=False)
        das.course = course

        payload = {
            "text": f"Гость оставил заявку на курс {course.title}\nЕго зовут {das.name}\nЕго номер {das.phone}",
            "chat_id": '-1001519795077',
        }

        response = requests.post(url, json=payload)
        das.save()
        return redirect('/')
    return render(request, 'course_detail.html', {'course': course, 'form': ApplicationCourseForm, 'Facts': CourseFacts.objects.filter(course=pk), 'questions': questions})


def applmet(request, pk):
    form = ApplicationMeetForm(request.POST)
    das = form.save(commit=False)
    qwe = Meeting.objects.get(id=pk)
    das.meeting = qwe
    payload = {
        "text": f"Гость оставил заявку на {qwe.title}\nЕго зовут {das.name}\nНомер телефона {das.phone}",
        "chat_id": '-1001519795077',
    }

    response = requests.post(url, json=payload)
    form.save()
    return redirect('/')





