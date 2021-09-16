from django.urls import path

from core.erp.views import myfirstview, mysecondview

app_name = 'erp'

urlpatterns = [
    path('uno/', myfirstview, name='Vista1'),
    path('dos/', mysecondview, name='Vista2')
]