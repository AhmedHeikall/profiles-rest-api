from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework import status, viewsets
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns a List of APIView features"""

        an_apiview = [
            "Uses HTTP methods as a functions (get, post, put, patch, delete)",
            "Is similar to traditional django view",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLS",
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""

        return Response({"message": "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of on object"""

        return Response({"message": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({"message": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and ubdating profiles"""

    serializer_class = serializers.UserProfileSerializers
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnPrifile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "name",
        "email",
    )


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
