from django.http import HttpResponse

def helloworldfunction(request):
    return HttpResponse('<h1>hello world</h>')