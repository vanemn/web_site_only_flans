"""onlyflans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from web.views import index, about,welcome,cart, checkout,updateItem,contact
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Ruta para el índice
    path('about/', about, name='about'),  # Ruta para acerca
    path('welcome/', welcome, name='welcome'),  # Ruta para bienvenido cliente
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', updateItem, name="update_item"),
    path('accounts/',include('django.contrib.auth.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)