from django.http import HttpResponse
from django.shortcuts import render
import requests

base_url = 'http://localhost:8080/'


def wmts(request):
    print(request)
    url = base_url+'geoserver/gis/wms?service=WMS&request=GetMap&layers='+request.GET['layers']+\
        '&styles=&format='+request.GET['format']+'&transparent='+request.GET['transparent']+\
          '&version='+request.GET['version']+'&width='+request.GET['width']+'&height='+request.GET['height']+\
          '&srs='+request.GET['srs']+'&bbox='+request.GET['bbox']
    if 'CQL_FILTER' in request.GET:
        url = url + '&CQL_FILTER=' + request.GET['CQL_FILTER']
    print(url)
    image_data = requests.get(url=url,stream=True)
    return HttpResponse(image_data,content_type='image/png')


# wmts
def terzone_wmts(request):
    return render(request,'terzone/terzone_wmts.html')


# def getfeature(request):
#     url = base_url + 'geoserver/wfs?request=GetFeature&version=1.1.0&typeName='+request.GET['typeName']+'&outputFormat=application%2Fjson'
#     if 'BBOX' in request.GET:
#         url = url + '&BBOX=' + request.GET['BBOX']
#     if 'CQL_FILTER' in request.GET:
#         url = url + '&CQL_FILTER=' + request.GET['CQL_FILTER']
#     print(url)
#     json_data = requests.get(url=url)
#     return HttpResponse(json_data,content_type='application/json')
#
#
# # box_feature
# def bbox_feature(request):
#     return render(request,'terzone/bbox_feature.html')
#
#
# # attr_feature
# def attr_feature(request):
#     return render(request,'terzone/attr_feature.html')


