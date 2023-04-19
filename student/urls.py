from django.urls import path

from student import views

app_name = 'student'

urlpatterns = [
    path('',views.home,name='home'),
    path('result/',views.result,name='result'),
]