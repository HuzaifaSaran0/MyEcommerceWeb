# from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from .models import Product, Contact, Email, Order, Order_Update
from math import ceil
import json
# from django.contrib.auth.forms import UserCreationForm

from .forms import create_user_form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# from django.contrib.auth.models import User


@login_required(login_url='login')
def index(request):
    email = request.POST.get('email', '')
    if request.method == 'POST':
        Email(email=email).save()

    allProds = []
    cat_prods = Product.objects.values('category')
    cats = {item['category'] for item in cat_prods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = ceil(n / 1)  # 1, 2, 4
        allProds.append([prod, range(1, nSlides), nSlides])  # Fix range to include nSlides
    params = {'allProds': allProds}

    return render(request, "shop/index.html", params)


# def index(request):
#     products= Product.objects.all()
#     n= len(products)
#     nSlides= n//4 + ceil((n/4) + (n//4))
#     params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
#     return render(request,"shop/index.html", params)

def about(request):
    return render(request, 'shop/about.html')


@login_required(login_url='login')
def contact(request):
    the_thank = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        email2 = request.POST.get('email2', '')
        if name and email and phone and desc:
            the_thank = True
            Contact(name=name, email=email, phone=phone, desc=desc).save()
        elif email2:
            Email(email=email2).save()
    return render(request, 'shop/contact.html', {'the_thank': the_thank})


@login_required(login_url='login')
def tracker(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        order_id = request.POST.get('order_id', '')
        Email(email=email).save()
        try:
            order = Order.objects.filter(order_id=order_id, email=email)
            # print(order)
            # print(order[0])
            # print(order[1])

            if len(order) > 0:
                update = Order_Update.objects.filter(order_id=order_id)
                updates = []
                response = None
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.time_stamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')


def searchMatch(query, item):
    description = getattr(item, 'description', '') or ''
    product_name = getattr(item, 'product_name', '') or ''
    category = getattr(item, 'category', '') or ''
    if query in description or query in product_name or query in category:
        return True
    return False


def search(request):
    query = request.GET.get('search')
    email = request.POST.get('email', '')
    if request.method == 'POST':
        Email(email=email).save()

    allProds = []
    cat_prods = Product.objects.values('category')
    cats = {item['category'] for item in cat_prods}
    for cat in cats:
        prod_temp = Product.objects.filter(category=cat)
        prod = [item for item in prod_temp if searchMatch(query, item)]
        n = len(prod)
        nSlides = ceil(n / 1)  # 1, 2, 4
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])  # Fix range to include nSlides
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0:
        params["msg"] += "No Product with such name couldn't found. Try Searching Different inputs."
        return render(request, 'shop/search.html', params)
    return render(request, 'shop/search.html', params)



@login_required(login_url='login')
def product_view(request, myid):
    email = request.POST.get('email', '')

    if request.method == 'POST':
        Email(email=email).save()
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    # print(product)
    return render(request, 'shop/product_view.html', {'product': product[0]})


thank = False


@login_required(login_url='login')
def checkout(request):
    global thank
    if request.method == 'POST':
        thank = True
        json_items = request.POST.get('json_items', '')
        amount = request.POST.get('amount')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')
        address2 = request.POST.get('address2', '')
        country = request.POST.get('country', '')
        city = request.POST.get('city', '')
        zip_code = request.POST.get('zip', '')
        name_on_credit = request.POST.get('name_on_credit', '')
        credit_number = request.POST.get('credit_number', '')
        expiry = request.POST.get('expiry', '')
        CVV = request.POST.get('CVV', '')

        if first_name and last_name and phone and email and address and country and city and zip_code and \
                name_on_credit and credit_number and expiry and CVV and json_items:
            amount = int(amount)
            phone = int(phone)
            zip_code = int(zip_code)
            credit_number = int(credit_number)
            CVV = int(CVV)
            order = Order(items_json=json_items, amount=amount, first_name=first_name, last_name=last_name, email=email,
                          phone=phone, address=address, address2=address2,
                          city=city, country=country, zip_code=zip_code, name_on_credit=name_on_credit,
                          credit_number=credit_number, expiry=expiry, CVV=CVV)
            order.save()
            update = Order_Update(order_id=order.order_id, update_desc="The Order has been Placed")
            update.save()
            id_ = order.order_id

            return render(request, 'shop/checkout.html', {"thank": thank, "id_": id_})
        # else:
        #     # return render(request, 'shop/checkout.html', {"thank": thank})
        #     return redirect('checkout', {thank})
    return render(request, 'shop/checkout.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('/shop')
    else:
        form = create_user_form()
        if request.method == "POST":
            form = create_user_form(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created for " + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'shop/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/shop')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/shop')
            else:
                messages.info(request, 'username or password is incorrect')
                # return render(request, 'shop/login.html')

        context = {}
        return render(request, 'shop/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')

# def login(request):
# if request.method == "POST":
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#
# return render(request, 'shop/login.html')


# def register(request):
#     if request.method == "POST":
#         first_name = request.POST.get('first_name', '')
#         last_name = request.POST.get('last_name', '')
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = User.objects.create_user(
#             first_name=first_name,
#             last_name=last_name,
#             username=username
#         )
#         user.set_password(password)
#         user.save()
#         return redirect('/register/')

# return render(request, 'shop/register.html')
