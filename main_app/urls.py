from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('finches/', views.finches_index, name="index"),
    path('finches/<int:finch_id>/', views.finches_detail, name="detail"),
    path('finches/<int:finch_id>/add_siting/', views.add_siting, name="add_siting"),
    path('finches/create/', views.FinchCreate.as_view(), name="finches_create"),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name="finches_update"),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name="finches_delete"),
    path('nests/', views.NestList.as_view(), name='nests_index'),
    path('nests/create/', views.NestCreate.as_view(), name='nests_create'),
    path('nests/<int:pk>/update/', views.NestUpdate.as_view(), name="nests_update"),
    path('nests/<int:pk>/delete/', views.NestDelete.as_view(), name="nests_delete"),

]