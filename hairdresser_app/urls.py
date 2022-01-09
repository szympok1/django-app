from django.contrib import admin
from django.urls import path
from app.views import redirect_home, index, new_reservation, staff_profile, user_profile, login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index),
    path('login/', login_view),
    path('register/', register_view),
    path('userprofile/', user_profile),
    path('newreservation/', new_reservation),
    path('staffprofile/', staff_profile),
    path('logout/', logout_view),
    path('', redirect_home),
]