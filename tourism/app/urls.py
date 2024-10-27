from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('booking/<str:resort_name>/<str:room_id>', views.form, name='form'),
    path('resort/', views.resort, name='resort'),
    path('resort/<int:id>/', views.resort_detail, name='resort_detail'),
    path('book/',views.booking, name='booking')
]