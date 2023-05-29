""" from django.shortcuts import render, redirect
from django.http import request, QueryDict
from bson import json_util,
import json
from  Users_Management.MongoCRUD import MongoCheck, MongoGetUserData, MongoGetAllUsers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 



class Dashboard(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        #authentication_classes = (SessionAuthAll,)
        query = request.data
        print(query)
        if MongoCheck(query).user_exists():
            user_data = MongoGetUserData(query).getData()
            return Response(json.loads(json_util.dumps(user_data)))
        return Response("User not found") """