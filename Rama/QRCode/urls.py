from django.urls import path
from .views import generateQRCode,read_QRCode_url
urlpatterns = [
    path('generate_qr_code/', generateQRCode),
    path('read_qr_code_url/<str:url_token_numbers>', read_QRCode_url)
    
]
