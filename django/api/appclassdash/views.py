from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import InterestSerializer, UserSerializer, CourseSerializer
from .models import Interest, Course
from django.contrib.auth.models import User
from rest_framework import viewsets




class InterestViewSet(viewsets.ModelViewSet):
	serializer_class = InterestSerializer
	permission_classes = (permissions.IsAuthenticated,)
	def  get_queryset(self):
		if self.request.user.is_superuser:
			return Interest.objects.all()
		else:
			return Interest.objects.filter(id=self.request.user.id)

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer


class UserViewSet(viewsets.ModelViewSet):
	def get_queryset(self):
		if self.request.user.is_superuser:
			return User.objects.all()
		else:
			return User.objects.filter(id=self.request.user.id)
	serializer_class = UserSerializer

class HomePageView(TemplateView):
	template_name = "index.html"
