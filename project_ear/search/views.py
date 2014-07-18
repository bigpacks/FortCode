from django.http import HttpResponse


def index(request):
    return HttpResponse("World This Is It")