from django.urls import path
from accounts.views import get_profiles_list, get_profile, add_profile

app_name = 'accounts'

urlpatterns = [
    path('', get_profiles_list, name='list'),
    path('add/', add_profile, name='add'),
    path('show/<id>', get_profile, name='show'),
]
