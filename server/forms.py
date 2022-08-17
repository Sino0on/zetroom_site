from django import forms
from .models import *


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'call-to-action__inner-name', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'call-to-action__inner-phone', 'placeholder': 'Номер телефона'}),
        }


class ApplicationCourseForm(forms.ModelForm):
    class Meta:
        model = ApplicationCourse
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'course-call-to-action__right-name', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'course-call-to-action__right-tel', 'placeholder': 'Номер телефона'}),
        }


class ApplicationMeetForm(forms.ModelForm):
    class Meta:
        model = ApplicationMeeting
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'events_name', 'placeholder': 'Имя'}),
            'phone': forms.TextInput(attrs={'class': 'events_phone', 'placeholder': 'Номер телефона'}),
        }