from rest_framework.response import Response
from rest_framework.views import APIView

class HealthCheckView(APIView):
    def get(self, request):
        return Response({
            "status": "ok",
            "version": "1.0.0",
            "message": "API is healthy and running."
        })