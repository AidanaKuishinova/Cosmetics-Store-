"""faceit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('cart/', views.get_cart, name='cart'),
    path('cart/add/<uuid:id>/', views.add_to_cart, name='cartadd'),
    path('categories/<str:category>', views.categories, name="categories"),
    path('filter/', views.filter, name='filter'),
    path('search_items/', views.search_items, name='searching_products'),
    path('search_success/<str:text>', views.SearchSuccesView.as_view(), name='search_success'),
    path('inst/', views.inst, name='inst'),
    path('product/<uuid:id>',views.product_detail, name = 'product_detail')
]
