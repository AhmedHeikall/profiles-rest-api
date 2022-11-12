from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """Returns a List of APIView features"""

        an_apiview = [
            "Uses HTTP methods as a functions (get, post, put, patch, delete)",
            "Is similar to traditional django view",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLS",
        ]

        return Response({"message": "Hello!", "an_apiview": an_apiview})
