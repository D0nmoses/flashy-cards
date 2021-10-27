from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.apiOverview,name='apiOverview'),
    path('api/card-list',views.cardList,name='cardList'),
    path('api/card-detail/<str:pk>/',views.cardDetail,name='cardDetail'),
    path('api/card-create/',views.cardCreate,name='cardCreate'),
    path('api/card-update/<str:pk>/',views.cardUpdate,name='cardUpdate'),
]