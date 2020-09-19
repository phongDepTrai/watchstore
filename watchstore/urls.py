"""watchstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from mystore import views
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Quản trị của hàng"
admin.site.index_title = "Quản trị của hàng"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^mystore/', include('mystore.urls')),
    url(r'^cart/', include('cart.urls')),
    path('users/', include('django.contrib.auth.urls')),
    url(r'^orders/', include('orders.urls', namespace="orders")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)