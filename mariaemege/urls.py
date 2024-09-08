from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views  # Asumiendo que tienes una app llamada "myapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),  # Definirás esta vista para registro
]
