from django.urls import path

from enderecos.api.views import api_detail_enderecos

app_name = "endereco"

urlpatterns = [
    path("<id>/", api_detail_enderecos, name="detail"),
]
