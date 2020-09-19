from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from mystore.models import Product
from cart import forms 
from mystore.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index_default(request):
    all_pro_list = Product.objects.order_by('code')
    # pagination: 20 products per page
    paginator = Paginator(all_pro_list, 20)
    # get page number
    page_number = request.GET.get('page')
    pro_list = paginator.get_page(page_number)
    amount = len(all_pro_list)
    pro_dict = {"products":pro_list, "amount": amount }
    return pro_dict


def index(request, sort=0):
    if sort==0:
        all_pro_list = Product.objects.order_by('code')
    elif sort==1:
        all_pro_list = Product.objects.order_by('fee')
    elif sort==2:
        all_pro_list = Product.objects.order_by('fee').reverse()
    elif sort==3:
        all_pro_list = Product.objects.order_by('created')
    elif sort==4:
        if request.method == "POST":
            pattern = request.POST.get("search")
            all_pro_list = Product.objects.filter(name__contains=pattern)
        else:
            all_pro_list = Product.objects.order_by('code')
    elif sort==5:
        all_pro_list = Product.objects.filter(brand__contains='SEIKO')
    elif sort==6:
        all_pro_list = Product.objects.filter(brand__contains='FREDERIQUE CONSTANT')
    elif sort==7:
        all_pro_list = Product.objects.filter(brand__contains='TISSOT')
    elif sort==8:
        all_pro_list = Product.objects.filter(sex=1)
    elif sort==9:
        all_pro_list = Product.objects.filter(sex=2)
    elif sort==10:
        all_pro_list = Product.objects.filter(sex=4)
        
    # pagination: 20 products per page
    paginator = Paginator(all_pro_list, 20)

    # get page number
    page_number = request.GET.get('page')
    pro_list = paginator.get_page(page_number)
    amount = len(all_pro_list)
    pro_dict = {"products":pro_list, "amount": amount }
    return render(request, "mystore/index.html", context=pro_dict)


def product_detail(request, id=None):
    product = Product.objects.get(pk=id)
    # Sex
    if int(product.sex) == 1:
        product.sex = 'Nam'
    elif int(product.sex) == 2:
        product.sex = 'Nữ'
    else:
        product.sex = 'Khác'

    # Category
    if int(product.category) == 1:
        product.category = 'Đồng hồ cơ   '
    elif int(product.category) == 2:
        product.category = 'Đồng hồ điện tử'

    cart_product_form = forms.CardAddProductForm()
    return render(request, 'mystore/product_detail.html', context= {'product': product,'cart_product_form': cart_product_form})


def register(request):
    registered = False
    if request.method == "POST":
        form_user = UserForm(data = request.POST)
        form_por = UserProfileInfoForm(data = request.POST)
        if form_user.is_valid() and form_por.is_valid():
            user = form_user.save()
            user.set_password(user.password)
            user.save()

            profile = form_por.save(commit = False)
            profile.user = user

            print(request.FILES)
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(form_user.errors, form_por.errors)
    else:
        form_user = UserForm()
        form_por = UserProfileInfoForm() 
    return render(request, "mystore/registration.html", {'user_form':form_user,'profile_form': form_por,'registered': registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                pro_dict = index_default(request)
                return render(request, "mystore/index.html", context=pro_dict)
        else:
            print("Không đăng nhập được")
            print("Username: {} and password: {}".format(username, password))
            login_result = "Username và password không hợp lệ"
            return render(request, "mystore/login.html",{"login_result": login_result})
    else:
        return render(request, "mystore/login.html")


@login_required
def user_logout(request):
    logout(request)
    login_result = "Bạn đã đăng xuất. Vui lòng chọn 'Đăng nhập'"
    return render(request, "mystore/login.html",{"login_result": login_result})

