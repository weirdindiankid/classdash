from django.urls import path
from rest_framework import routers
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import InterestViewSet, UserViewSet, CourseViewSet 
from rest_framework.authtoken.views import obtain_auth_token



router = routers.DefaultRouter()
router.register(r'interests',InterestViewSet, 'interests')
router.register(r'courses', CourseViewSet, 'courses')
router.register(r'users', UserViewSet, 'users')

urlpatterns = [ url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^get-token/', obtain_auth_token), url(r'^', include(router.urls)), 
]

