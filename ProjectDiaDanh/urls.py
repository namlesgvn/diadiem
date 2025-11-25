# ProjectDiaDanh/urls.py

from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Liên kết ứng dụng locations (bao gồm cả trang chủ)
    path('', include('locations.urls')), 
]

# 2. CHỈ DÙNG TRONG MÔI TRƯỜNG PHÁT TRIỂN (Debug=True)
if settings.DEBUG:
    # Đoạn này phải nằm cuối cùng trong urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
