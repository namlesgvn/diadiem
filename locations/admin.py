# locations/admin.py

from django.contrib import admin
from .models import DiaDiem

@admin.register(DiaDiem)
class DiaDiemAdmin(admin.ModelAdmin):
    list_display = ('ten', 'loai', 'vido', 'kinhdo', 'ngay_cap_nhat')
    list_filter = ('loai',)
    search_fields = ('ten', 'mo_ta')
    
    fieldsets = (
        (None, {
            'fields': ('ten', 'loai', 'mo_ta', 'hinh_anh_dai_dien')
        }),
        ('Thông Tin Bản Đồ', {
            'fields': ('vido', 'kinhdo'),
            'description': 'Nhập tọa độ Vĩ độ và Kinh độ thủ công.'
        }),
    )
