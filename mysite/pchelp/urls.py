from django.urls import path

from .views import index , contact_us , ty

urlpatterns = [
    path('', index , name = 'index'),
    path('add' , contact_us , name = 'add'),
    path('add/ty', ty , name = 'ty')
]
