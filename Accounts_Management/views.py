
from django.shortcuts import redirect, render

# Create your views here
from rest_framework.views import APIView
from .MongoCRUD import MongoAccountStatus
from Users_Management.MongoCRUD import MongoGetUserData


def blockAccount(request):
    if request.method == "POST":
        if request.user.is_authenticated and request.user.is_staff:
            data = dict(request.POST.dict())
            del data['csrfmiddlewaretoken']

            """ MongoAccountStatus().blockAccount(data)

            user = MongoGetUserData(data)
            the_user = user.getData()
            account = user.getAccountData()
            return render(request, 'profile.html', {"user": the_user, "account": account}) """
            return redirect('user-profile')

    return redirect('login-page')

def enableAccount(request):
    if request.method == "POST":
        if request.user.is_authenticated and request.user.is_staff:
            data = dict(request.POST.dict())
            del data['csrfmiddlewaretoken']

            MongoAccountStatus().blockAccount(data)

            user = MongoGetUserData(data)
            the_user = user.getData()
            account = user.getAccountData()
            return render(request, 'profile.html', {"user": the_user, "account": account})
                  
            #return redirect('')

    return redirect('login-page')

    

    

