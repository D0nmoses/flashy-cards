from django.urls import path
import .views

urlpatterns = [
    path('api/',views.apiOverview,name='apiOverview')
]