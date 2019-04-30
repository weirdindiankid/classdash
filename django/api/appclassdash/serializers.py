from rest_framework import serializers
from .models import Interest
from .models import Course
from django.contrib.auth.models import User


class InterestSerializer(serializers.ModelSerializer):

	owner = serializers.ReadOnlyField(source = 'owner.username')
	course = serializers.ReadOnlyField(source = 'course.code')

	class Meta:
		model = Interest
		fields = ('id', 'owner', 'course', 'created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):


	class Meta:
		model = User
		fields = ('id', 'username')


class CourseSerializer(serializers.ModelSerializer):


	class Meta:
		model = Course
		fields = ('id', 'code', 'section', 'name', 'semester', 'seats', 'instructor', 'created_at', 'updated_at',)

