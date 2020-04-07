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
    path('similar/create/', views.SimilarCreate.as_view(), name="similar_create"),
    path('similar/<int:pk>/delete/', views.SimilarDelete.as_view(), name="similar_delete"),
    path('similar/<int:pk>/update/', views.SimilarUpdate.as_view(), name="similar_update"),
    path('finches/<int:finch_id>/assoc_finch/<int:similar_id>/', views.assoc_finch, name="assoc_finch"),
    path('finches/<int:finch_id>/disassoc_finch/<int:similar_id>/', views.disassoc_finch, name="disassoc_finch"),
    path('finches/<int:finch_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name="signup"),
]