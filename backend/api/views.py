import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    # requset -> HttpRequest-> Django
    # print(dir(request))
    # request.body
    print(request.GET) #url query params
    print(request.POST) #
    body = request.body #by string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> python dict
        #Để chuyển đổi chuỗi bytes này thành một đối tượng JSON trong Python, ta có thể sử dụng module json của Python và phương thức loads() để phân tích cú pháp JSON
    except:
        pass
    print(data)
    #data['headers'] = request.headers #request.META
    data['params']= dict(request.GET)
    data['headers']= dict(request.headers)
    data['content_type'] = request.content_type
    
    #context={"message":"day la demo api"}
    return JsonResponse(data)