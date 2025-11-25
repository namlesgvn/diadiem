# locations/serializers.py

from rest_framework import serializers
from .models import DiaDiem

class DiaDiemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaDiem
        # Chỉ lấy các trường cần thiết cho bản đồ và hiển thị cơ bản
        fields = ['id', 'ten', 'loai', 'vido', 'kinhdo', 'hinh_anh_dai_dien']
