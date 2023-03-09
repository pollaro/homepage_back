import json

from django.http import HttpResponse
from rest_framework.views import APIView


class HomeView(APIView):
    def get(self, request):
        if request.session and "token" in request.session:
            return HttpResponse(
                json.dumps(
                    {
                        "token": request.session["token"],
                    }
                )
            )
        return HttpResponse(status=200)
