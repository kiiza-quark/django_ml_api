from django.shortcuts import render
from .views import *
# Create your views here.

import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response


class Prediction(APIView):
    def post(self, request):
        #data = request.data
        age= request.POST.get('age')
        gender = request.POST.get('gender')
        bp = request.POST.get('bp')
        cholesterol = request.POST.get('cholesterol')
        salt = request.POST.get('salt')
        dtree = ApiConfig.model
        #predict using independent variables
        PredictionMade = dtree.predict([[age, gender, cholesterol, bp, salt]])
        response_dict = {"Predicted drug": PredictionMade}
        print(response_dict)
        return Response(response_dict, status=200)
