from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html/', views.about, name='about'),
    path('products.html/', views.products, name='products'),
    path('store.html/', views.store, name='store'),
]
