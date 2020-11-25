from django.contrib import admin
from django.urls import path, include

import enderecos
from enderecos.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),

    # REST FRAMEWORK URLS
    path("api/endereco/", include("enderecos.api.urls", "endereco_api")),
]
