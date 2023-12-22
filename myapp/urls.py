# myapp/urls.py
from django.urls import path
from .views import gcd_lcm

urlpatterns = [
    path('gcd_lcm/', gcd_lcm, name='gcd_lcm'),
]
