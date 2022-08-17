from django.shortcuts import render
from .models import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .filters import *
from django_filters import rest_framework as filters


class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class AccountListView(generics.ListAPIView):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = AccountListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StudentFilter


class SuperAccountListView(generics.ListAPIView):
    queryset = Account.objects.filter(is_staff=True)
    permission_classes = (AllowAny,)
    serializer_class = AccountListSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CourseListSerializer


class ApplicationView(generics.ListAPIView):
    queryset = Application.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ApplicationListSerializer


class MettingView(generics.ListAPIView):
    queryset = Meeting.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = MeetingListSerializer


class ApplicationDeleteView(generics.DestroyAPIView):
    queryset = Application.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ApplicationListSerializer
    lookup_field = 'id'


class MeetApplicationView(generics.ListAPIView):
    queryset = ApplicationMet.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = MeetApplicationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MeetApplFilter


class MeetOnlyApplicationView(generics.ListAPIView):
    queryset = ApplicationMet.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = MeetApplicationSerializer
    lookup_field = 'id'


class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = GroupListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GroupFilter

    # def get_serializer_context(self):
    #     return super().get_serializer_context().update({'account_tg': self.request.data['account']})


class GroupbotListView(generics.ListAPIView):
    queryset = Group.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = GroupUpdateSerializer


class GroupUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Group.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = GroupUpdateSerializer
    lookup_field = 'pk'


class Onlu(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = ApplicationCreateAPI(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        else:
            Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)


class ApplicationMetCreate(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializers = ApplicationMetAPI(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
        else:
            Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)