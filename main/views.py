
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
import random
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import AuthUserForm, RegisterUserForm
from .models import Product,Category,ProductItem,Cart
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    context={}
    products=Product.objects.all()
    products=list(products)
    random.shuffle(products)
    context['products']=products[:4]

    context['popular'] = products[85:93]

    return  render(request, 'main/index.html',context)

def inst(request):
    return render(request, 'main/inst.html')


def payment(request):
    return render(request, 'main/payment.html')

def categories(request, category):
    category2 = Category.objects.get(url=category)
    products=Product.objects.filter(category=category2)
    prices=[]
    brands=set()
    countries = set()

    for product in products:
        try:
            prices.append(product.price)
            if "Ингредиенты:" in product.brand:
                continue
            brands.add(product.brand)
            country = product.country
            # country = country.strip()
            countries.add(country)
        except:
            continue
            pass
    contex = {
        'title':category2.title,
        'products': products,
        'minprice':min(prices),
        'maxprice':max(prices),
        'brands':brands,
        'countries':countries
    }
    return render(request, 'main/category.html', contex)

def category(request):
    return render(request, 'main/category.html', contex)

def get_cart(request):
    user = User.objects.get(username=request.user.username)
    cart = Cart.objects.get(user=user)
    items=ProductItem.objects.filter(cart=cart)
    all_products=0
    for item in items:
        print(item.__dict__)
        quantity=item.quantity
        price=item.product.price
        all_products=all_products+(quantity*price)
    contex={
         'items':items,
        'allproducts':all_products
     }
    return render(request,"main/cart.html",contex)


def add_to_cart(request,id):
    print(id)
    user=User.objects.get(username=request.user.username)
    product=Product.objects.get(id=id)
    cart=Cart.objects.get(user=user)
    product_item=ProductItem(product=product,cart=cart)
    if ProductItem.objects.filter(product=product,cart=cart).exists():
        ps=ProductItem.objects.filter(product=product,cart=cart)
        for p in ps:
            p.quantity+=1
            p.save()
            print("222")
    else:
        product_item.save()

    return redirect("cart")

def delete_from_cart(request,id):
    print(id)
    user = User.objects.get(username=request.user.username)
    product = Product.objects.get(id=id)
    cart = Cart.objects.get(user=user)

    ProductItem.objects.filter(product=product,cart=cart).delete()
    return redirect("cart")


def register(request):
    username=request.POST.get("username")
    password = request.POST.get("password")
    user=User(username=username)
    user.set_password(password)
    user.save()

    return redirect("login")

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
    searched = request.POST.get('searched')
    print(searched)
    request.session['searched'] = searched
    contex = {

        'searched':searched
    }
    return redirect(f'/search_success/{searched}', searched=searched)

class SearchSuccesView(ListView):
    template_name="main/search_items.html"
    paginate_by = 12
    context_object_name = 'items_list'

    def get_queryset(self):
        search_text = self.request.path.split('/')[-1]
        return Product.objects.filter(description__iregex=search_text)

def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'main/product_detail.html', {'data':product})

