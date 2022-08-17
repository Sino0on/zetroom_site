from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
import requests

url = "https://api.telegram.org/bot5346235377:AAGg1mWc4FPRxGn1GFcnOBcj75MMLlrAJlA/sendMessage"


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Account.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ('username', 'username_tg', 'password', 'password2', 'email', 'first_name', 'last_name', 'tg')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'tg': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Account.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            tg=validated_data['tg'],
            username_tg=validated_data['username_tg']
        )

        user.set_password(validated_data['password'])
        user.save()
        payload = {
            "text": f"Вы успешно зарегистрировались✅\nВаш никнейм {validated_data['username']}\nВаш пароль {validated_data['password'][0:3]}{(len(validated_data['password'])-3)*'*'}",
            "chat_id": validated_data['tg'],
        }

        response = requests.post(url, json=payload)
        payload = {
            "text": f"Только что зарегистрировался человек по имени {validated_data['first_name']} {validated_data['last_name']} \nЕго ТГ {validated_data['username_tg']}",
            "chat_id": '-1001519795077',
        }

        response = requests.post(url, json=payload)
        return user


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudensSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'


class MeetApplicationSerializer(serializers.ModelSerializer):
    # account = StudensSerializer(many=True)

    class Meta:
        model = ApplicationMet
        fields = '__all__'


class GroupListSerializer(serializers.ModelSerializer):
    students = StudensSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'


class GroupUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class ApplicationListSerializer(serializers.ModelSerializer):
    account = StudensSerializer()
    course = CourseListSerializer()

    class Meta:
        model = Application
        fields = ['id', 'account', 'course', 'date']


class MeetingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = '__all__'


class ApplicationCreateAPI(serializers.Serializer):

    account = serializers.IntegerField()
    course = serializers.IntegerField()

    def create(self, validated_data):
        account = Account.objects.get(tg=validated_data['account'])
        course = Course.objects.get(id=validated_data['course'])

        application = Application(
            account=account,
            course=course
        ).save()

        payload = {
            "text": f"Только что оставили заявку на курс по {course.title} {account.first_name}\nЧеловек по имени {account.last_name}\nЕго тг {account.username_tg}",
            "chat_id": '-1001519795077',
        }

        response = requests.post(url, json=payload)

        return {}


class ApplicationMetAPI(serializers.Serializer):
    account = serializers.IntegerField()
    meeting = serializers.IntegerField()

    def create(self, validated_data):
        account = Account.objects.get(tg=validated_data['account'])
        meeting = Meeting.objects.get(id=validated_data['meeting'])

        application = ApplicationMet(
            account=account,
            meeting=meeting
        ).save()

        payload = {
            "text": f"Только что оставили заявку на мероприятие {meeting.title} {account.first_name}\nЧеловек по имени {account.last_name}\nЕго тг {account.username_tg}",
            "chat_id": '-1001519795077',
        }

        response = requests.post(url, json=payload)

        return {}