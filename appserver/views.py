from django.http import HttpResponse

def hello(request):
    query_string = request.META['QUERY_STRING'].split('&')
    response = '\n'.join(query_string)
    return HttpResponse(response)
