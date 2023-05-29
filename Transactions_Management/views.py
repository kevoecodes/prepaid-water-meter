""" from email import message
from django.shortcuts import render
from django.http import QueryDict
from bson import json_util
import json
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
from Users_Management.MongoCRUD import MongoGetUserData
from .MongoCRUD import MongoAddDeposit,MongoGetTransactions


class Deposit(APIView):
    permission_classes = ()
    def post(self, request, *args, **kwargs):
        user_dict = request.data
        user = QueryDict('', mutable=True)
        user.update(user_dict)

        return Response(True)

class GetUserTransactions(APIView):
    def post(self, request, *args, **kwargs):
        query = request.data

        transactions = MongoGetTransactions().getUserTransactions(query)
        
        return Response(json.loads(json_util.dumps(transactions)))


         """