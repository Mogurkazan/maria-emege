from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('image/<str:image_name>/', views.image_detail, name='image_detail'),
    path('signup/', views.signup, name='signup'),  
    path('category/<str:category_name>/', views.category_view, name='category'),
    path('add_to_cart/<str:image_name>/', views.add_to_cart, name='add_to_cart'),
]
