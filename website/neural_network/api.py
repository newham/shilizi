import json

from django.http import HttpResponse


def test(request):
    resp = {'code': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def query(request,name=''):
    print(name)
    resp = {'code': 0, 'label': 1}
    return HttpResponse(json.dumps(resp), content_type="application/json")
