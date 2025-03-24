from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    #path('mainpage/',views.mainpage,name="mainpage"),
    path('index/',views.index,name='index'),
    path('<str:short_code>/',views.index, name='redirect'),
]