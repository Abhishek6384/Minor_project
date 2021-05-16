from django.urls import path
from . import views


urlpatterns = [
     path('detect',views.detect_mask),
     path('detect_user',views.detect_mask_user),
]
