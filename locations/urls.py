# locations/urls.py

from django.urls import path
from .views import DiaDiemListAPIView, map_view, diadiem_detail # <-- Đã thêm diadiem_detail

urlpatterns = [
    path('', map_view, name='home'), 
    path('api/locations/', DiaDiemListAPIView.as_view(), name='diadiem-list-api'),
    # Đường dẫn cho trang chi tiết (sử dụng ID là số nguyên)
    path('diadiem/<int:pk>/', diadiem_detail, name='diadiem-detail'), 
]
