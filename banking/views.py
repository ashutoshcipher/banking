from django.shortcuts import render
from .models import Banks, Branches
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


def all_banks(request):
    banks = Banks.objects.all()[:5]
    return JsonResponse({'banks': banks})

def get_bank_detials_from_ifsc_code(request, ifsc):
    res = Branches.objects.filter(ifsc =ifsc).values('ifsc',
                                                     'bank__name',
                                                     'bank__id',
                                                     'branch',
                                                     'address',
                                                     'city',
                                                     'district',
                                                     'state')

    res = list(res)
    return JsonResponse({'data' : res})


@csrf_exempt
def get_bank_detials_from_name_and_city(request):

    name = request.POST.get('name', None)
    city = request.POST.get('city', None)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    name = body.get('name', None)
    city = body.get('city', None)

    if name is None and city is None:
        return JsonResponse({'message' : 'Invalid Request'})

    res = Branches.objects.filter(city=city, bank__name=name).values('ifsc',
                                                     'bank__name',
                                                     'bank__id',
                                                     'branch',
                                                     'address',
                                                     'city',
                                                     'district',
                                                     'state')

    res = list(res)
    return JsonResponse({'data': res})


