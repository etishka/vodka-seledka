from django.shortcuts import render
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    context = {}
    #return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)
