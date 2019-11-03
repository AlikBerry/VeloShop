from django.urls import path
from . import views


urlpatterns = [
    path("", views.baseindexview, name='home'),
    path("login/", views.login_view, name='login'),
    path('home/', views.homepage, name='base'),
    path('home/<int:id>', views.product_detail, name='product_detail')
      
]