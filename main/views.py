
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
import random
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import AuthUserForm, RegisterUserForm
from .models import Product,Category,ProductItem,Cart

# Create your views here.
def index(request):
    context={}
    products=Product.objects.all()
    products=list(products)
    random.shuffle(products)
    context['products']=products[:4]

    context['popular'] = products[85:93]

    return  render(request, 'main/index.html',context)


def categories(request, category):
    category2 = Category.objects.get(url=category)
    products=Product.objects.filter(category=category2)

    contex = {
        'title':category2.title,
        'products': products,
    }
    return render(request, 'main/category.html', contex)


def get_cart(request):
    user = User.objects.get(username=request.user.username)
    cart = Cart.objects.get(user=user)
    items=ProductItem.objects.filter(cart=cart)

    contex={
         'items':items
     }
    return render(request,"main/cart.html",contex)

def add_to_cart(request,id):
    print(id)
    user=User.objects.get(username=request.user.username)
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(user=user)
    product_item=ProductItem(product=product,cart=cart)
    product_item.save()

    return redirect("index")

def filter (request):
    return render(request,"main/filter.html")

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

def search_items(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        items = Product.objects.filter(title__iregex=searched)
        return render(request, "main/search_items.html",{'searched':searched,'items':items})
    else:
        return render(request, "main/search_items.html", {})