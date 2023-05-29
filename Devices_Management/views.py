from datetime import datetime
from bson import json_util, ObjectId
from pymongo import MongoClient
import json
from channels import layers
from channels.auth import _get_user_session_key
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
#from Channels_Manager.User_channel import PostToUserChannel

#from pymongo import response
from django.http import QueryDict
from Devices_Management.MongoCRUD import MongoDevicesManager
from Transactions_Management.MongoCRUD import MongoPurchaseWater, MongoUnitsUpdate
from rest_framework.response import Response
from rest_framework.views import APIView
#from User_Listen_Portal.consumer import User_Dev_Portal


class Device_Portal(APIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        #data = {}
        data = request.data
        print(type(data))
        if type(data) == QueryDict:
            data = dict(request.data.dict())
            print(type(data))

        print(data)
        device_manager = MongoDevicesManager()
        if device_manager.isDevice(data) and not device_manager.isBlocked(data):
            update = device_manager.deviceUpdate(data)
            if update == True:
                return Response(device_manager.new_units)

        return Response(False)

