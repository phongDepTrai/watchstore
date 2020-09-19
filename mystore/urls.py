from django.contrib import admin
from django.urls import path
from mystore import views
from django.conf.urls import url

app_name = "mystore"

urlpatterns = [
    path('<int:sort>/',views.index,name='index'),
    url(r'^$',views.index,name='index'),
    url(r'^product_detail/(\d+)/$', views.product_detail, name='product_detail'),
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^login/$',views.user_login,name='login'),
]