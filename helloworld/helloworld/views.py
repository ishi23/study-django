from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    return HttpResponse('<h1>hello world</h>')

# Djangoで用意されたテンプレートクラスを継承
class HelloWorldClass(TemplateView):
    template_name = 'hello.html'  # 探す場所はsettings.TEMPLATESのDIRSリストに指定
