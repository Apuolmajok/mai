from django.urls import path
from . import views

urlpatterns = [
        path('', views.Home, name='Home'),
        path('search/', views.search, name='search'),
        path('about/', views.about, name='about'),
        path('zzTandC/', views.zzTandC, name='zzTandC'),
        path('login/', views.login_user, name='login'),
        path('logout/', views.logout_user, name='logout'),
        path('register/', views.register_user, name='register'),
        path('update_password/', views.update_password, name='update_password'),
        path('update_user/', views.update_user, name='update_user'),
        path('update_info/', views.update_info, name='update_info'),
        path('business/', views.business, name='business'),
        path('product/<int:pk>', views.product, name='product'),
        path('category/<str:foo>', views.category, name='category'),
]