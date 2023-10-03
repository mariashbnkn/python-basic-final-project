from django.shortcuts import render

base_url = 'http://localhost:8080/'


def terzones_map(request):
    return render(request,'terzone/terzones_map.html')




