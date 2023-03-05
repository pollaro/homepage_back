from django.http import HttpResponse

def no_function(request):
    return HttpResponse(status=204)