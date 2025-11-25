# locations/views.py

from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework import filters # <-- Import cần thiết cho bộ lọc
from .models import DiaDiem
from .serializers import DiaDiemSerializer

# =================================================================
# 1. VIEWS FRONTEND (Hiển thị trang HTML)
# =================================================================

# View 1: Hiển thị Trang Bản đồ Chính (Trang chủ)
def map_view(request):
    """Render trang HTML chứa bản đồ Leaflet."""
    return render(request, 'locations/map_page.html', {})
    
# View 2: Hiển thị Trang Chi tiết Địa điểm
def diadiem_detail(request, pk):
    """Hiển thị thông tin chi tiết của một địa điểm dựa trên ID."""
    # Lấy đối tượng DiaDiem, nếu không tìm thấy sẽ trả về lỗi 404
    diadiem = get_object_or_404(DiaDiem, pk=pk)
    
    context = {
        'diadiem': diadiem
    }
    
    # Render template chi tiết
    return render(request, 'locations/diadiem_detail.html', context)


# =================================================================
# 2. API VIEWS (Cung cấp dữ liệu cho Frontend)
# =================================================================

# View 3: Lấy Danh sách Địa điểm (có hỗ trợ Lọc và Tìm kiếm)
class DiaDiemListAPIView(generics.ListAPIView):
    """
    Cung cấp danh sách các địa điểm.
    Hỗ trợ tìm kiếm theo tên/mô tả và sắp xếp.
    """
    queryset = DiaDiem.objects.all()
    serializer_class = DiaDiemSerializer
    
    # Thiết lập Bộ lọc
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    # Các trường cho phép tìm kiếm
    # Frontend có thể gọi: /api/locations/?search=Ha%20Noi
    search_fields = ['ten', 'mo_ta'] 
    
    # Các trường cho phép sắp xếp
    # Frontend có thể gọi: /api/locations/?ordering=-ngay_cap_nhat
    ordering_fields = ['ten', 'loai', 'ngay_cap_nhat']
    
    # Giá trị sắp xếp mặc định
    ordering = ['ten']
