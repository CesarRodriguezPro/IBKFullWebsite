"""IBKProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

https://www.ibktech.info/ret/xcd'code''date'
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('redirect', views.redirect_to, name='redirect_to'),
    path('hub/', include(('Main_Hub.urls', 'main_hub'))),
    path('accounts/', include(('accounts.urls', 'accounts'))),
    path('employees/', include(('employees.urls', 'employees'))),
    path('documents/', include(('documents.urls', 'documents'))),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
