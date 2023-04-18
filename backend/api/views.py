from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    
    context={"message":"day la demo api"}
    return JsonResponse(context)