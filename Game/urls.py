from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import include
from Game import views
urlpatterns = [

    path('Game/play',views.play,name="play"),
    path('validate',views.validate,name="validate"),
    # path('/redirect/',views.play,name="validate"),
    
]