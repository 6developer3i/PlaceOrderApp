from django.urls import path
from . import views

urlpatterns = [
    # path("show", views.show),
    path('login', views.login, name='index'),
    path('shopify', views.shopify),
    # path('get_token', views.get_token),
    path('final', views.final),
    # path('result', views.result),
    path('form', views.create),
    path('created_form', views.createdform),
    path('data', views.getdata, name='data'),
]
