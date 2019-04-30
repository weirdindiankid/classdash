
from rest_framework.permissions import BasePermission
from .models import Interest


class IsOwner(BasePermission):

	def has_object_permission(self, request, view, obj):
		if isinstance(obj, Interest):
			return obj.owner == request.user
		return obj.owner == request.user
