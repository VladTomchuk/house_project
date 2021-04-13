from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('success-request', home, name='home-valuate-property'),
    path('reforms', our_reforms, name='reforms'),
    path('services', services, name='services'),
    path('contacts', contacts, name='contacts'),
    path('property', all_property_search, name='property'),
    path('property/<int:property_id>/', view_property, name='view_property'),
    path('reforms/<int:reforms_id>/', view_our_reforms, name='view_our_reforms')
]
