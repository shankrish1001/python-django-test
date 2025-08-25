from django.contrib import admin
from django.urls import path
from my_test_app import views  # import your view here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.shantest),
]
