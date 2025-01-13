from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('booking/<str:resort_name>/<str:room_id>', views.form, name='form'),
    path('resort/', views.resort, name='resort'),
    path('resort/<int:id>/', views.resort_detail, name='resort_detail'),
    path('book/',views.booking, name='booking'),
    path('loginForm/',views.loginForm, name='loginForm'),
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('registerForm/',views.registerForm, name='registerForm'),
    path('create_user/', views.create_user_view, name='create_user'),
    path('auth/home', views.auth_home, name='auth_home'),
    path('settings/', views.resort_settings, name='resort_settings'),
    path('settings/room', views.room_page, name='room_page'),
    path('settings/add/room', views.add_room_view, name='add_room_view'),
    path('settings/room/form/<int:id>', views.update_room, name='update_room'),
    path('settings/room/delete/<int:id>', views.delete_room, name='delete_room'),
    path('festivals/', views.festivals, name='festivals'),
    path('events/', views.events, name='events'),
    path('activities/', views.activities, name='activities'),
    path('fiestas/', views.fiestas, name='fiestas'),
]