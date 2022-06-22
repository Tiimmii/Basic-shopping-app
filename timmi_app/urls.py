from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.products, name='products'),
    path('search', views.search, name='search'),
    path('signup',views.signup,name='signup'),
    path('login', views.login, name='login'),
]