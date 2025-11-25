# locations/models.py

from django.db import models

class DiaDiem(models.Model):
    LOAI_DIA_DIEM = (
        ('LS', 'Lịch Sử'),
        ('VH', 'Văn Hóa'),
        ('TN', 'Thiên Nhiên'),
    )

    ten = models.CharField(max_length=200, verbose_name="Tên Địa Điểm")
    loai = models.CharField(max_length=2, choices=LOAI_DIA_DIEM, verbose_name="Phân Loại")
    mo_ta = models.TextField(verbose_name="Mô Tả Chi Tiết")
    
    hinh_anh_dai_dien = models.ImageField(
        upload_to='diadiem_images/', 
        blank=True, 
        null=True, 
        verbose_name="Ảnh Đại Diện"
    )
    
    # Thông tin Bản đồ (nhập thủ công)
    vido = models.FloatField(
        verbose_name="Vĩ Độ (Latitude)",
        help_text="Nhập tọa độ Vĩ độ (ví dụ: 21.0285).",
        blank=True,
        null=True
    )
    kinhdo = models.FloatField(
        verbose_name="Kinh Độ (Longitude)",
        help_text="Nhập tọa độ Kinh độ (ví dụ: 105.8542).",
        blank=True,
        null=True
    )

    ngay_tao = models.DateTimeField(auto_now_add=True)
    ngay_cap_nhat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ten

    class Meta:
        verbose_name_plural = "Địa Điểm"
