from django.http import JsonResponse,HttpResponseRedirect,HttpResponseNotFound
from django.shortcuts import render
from .forms import Car_testing
from .models import Car_test
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
import io
from rest_framework.parsers import JSONParser
import json


class CarSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Car_test
        fields = ['car_id', 'color', 'year', 'manufacturer']
        extra_kwargs = {
                'color': {
                    'required': False,
                    'allow_null':True
                 },
                'year': {
                    'required': False,
                    'allow_null':True
                 },
                'manufacturer': {
                    'required': False,
                    'allow_null':True
                 }
            }
# получение данных из бд и создание объектов
def index(request):
    carform = Car_testing()
        
    if request.method == "POST":
        carform=Car_testing(request.POST)
        if carform.is_valid():
            
            car = Car_test()
            car.color = carform.cleaned_data["color"]
            car.year = carform.cleaned_data["year"]
            car.manufacturer = carform.cleaned_data["manufacturer"]
            car.save()
            return HttpResponseRedirect("/api/cars")
    car = Car_test.objects.all()
    
    car_Json = CarSerializer1(car,many=True)

    #JsonResponse(car_Json.data, safe=False) по URL
    return render(request, "1.html", {"car": car,"car_Json":json.dumps(car_Json.data, ensure_ascii=False)})



# изменение данных в бд, получение по ключу
@csrf_exempt #декоратор для временного оключения csrf token в случае запроса напрямую через URL
def edit(request, id):
    try:
        car = Car_test.objects.get(car_id=id)
        car_Json = CarSerializer1(car)
        if request.method == "DELETE":
            car.delete()
        elif request.method == "PATCH":
            a=request.body
            stream = io.BytesIO(a)
            data = JSONParser().parse(stream)
            serializer = CarSerializer1(car, data=data["json"], partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors)   
        return render(request, "2.html", {"car": car,"car_Json":car_Json.data})
    except Car_test.DoesNotExist:
        return HttpResponseNotFound("<h2>Car not found</h2>")
