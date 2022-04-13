
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import AuthUserForm, RegisterUserForm
from .models import Product,Category

# Create your views here.
def index(request):
    context={}
    category=Category.objects.get(title='Маски')
    products=Product.objects.filter(category=category)
    context['products']=products
    category = Category.objects.get(title='Сыворотки')
    products = Product.objects.filter(category=category)
    context['popular'] = products
    return  render(request, 'main/index.html',context)

def category(request):

    context={}
    category=Category.objects.get(title='Маски')
    products=Product.objects.filter(category=category)
    context['products']=products

    return  render(request, 'main/category.html',context)


def get_cart(request):
    return render(request,"main/cart.html")



class MyLoginView(LoginView):
    template_name = "main/login.html"
    form_class = AuthUserForm
    success_url = reverse_lazy('index')


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('index')

class RegisterUserView(CreateView):
    model = User
    template_name = "main/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    success_msg = "Пользователь успешно создан"

