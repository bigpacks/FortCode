from django.template import RequestContext
from django.shortcuts import render_to_response

def search(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('search/search.html', context_dict, context)