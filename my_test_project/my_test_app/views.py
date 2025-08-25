from django.http import HttpResponse

def shantest(request):
    return HttpResponse("<h4>Hi Shan, Welcome!</h4>")
