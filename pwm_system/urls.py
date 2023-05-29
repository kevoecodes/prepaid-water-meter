
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from Authentications.views import  RegisterUser, LoginUser, register_user, goToregister, LoginPage, login_request, Logout
from Devices_Management.views import Device_Portal
from Web_Views.views import changePrice, purchaseUnits, purchaseUnits_Page, viewMembers, viewUser, Dashboard_View, \
    DepositCash, editUser, deleteUser, editUserPassword

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    
    #Authentications process endpoints
    path('api/register-user', RegisterUser.as_view(), name="register-user"),
    path('api/login-user', LoginUser.as_view(), name="login-user"),
    path('api/api-token-auth/', obtain_auth_token, name='api_token_auth'),

    #Admin
    path('register-user-page', goToregister, name='register-user-page'),
    path('register-user', register_user, name='register-user'),
    path('login-page', LoginPage, name='login-page'),
    path('login-account', login_request, name='login-account'),
    path('logout', Logout, name='logout'),
    path('', Dashboard_View, name='admin-dashboard'),
    path('view-members', viewMembers, name='view-members'),
    path('user-profile/<str:id>', viewUser, name='user-profile'),
    path('edit-user/<str:id>', editUser, name='edit-user'),
    path('edit-user', editUser, name='edit-user'),
    path('change-password/<str:id>', editUserPassword, name='change-password'),
    path('change-password', editUserPassword, name='change-password'),
    path('delete-user', deleteUser, name='delete-user'),
    #path('deposit-cash-page', DepositPage, name="deposit-cash-pasge"),
    path('deposit-cash/<str:id>', DepositCash, name="deposit-cash"),
    path('change-price', changePrice, name='change-price'),

    #User purchasees
    path('purchase-page', purchaseUnits_Page, name='purchase-units-page'),
    path('purchase-units', purchaseUnits, name='purchase-units'),
    
    ###----Vending devices endpoints----###
    path('device-update-portal', Device_Portal.as_view(), name='device-update-portal'),
]
