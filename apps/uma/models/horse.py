from django.db import models
import os
from django.conf import settings


def get_horse_image_choices():
    """
    自動讀取 static/horses/ 裡的所有圖片，
    轉成 Django choices 格式。
    """
    folder = os.path.join(settings.BASE_DIR, 'static', 'horses')
    if not os.path.exists(folder):
        return []
    return [
        (f"horses/{f}", f.replace('.png', '').replace('_', ' '))
        for f in os.listdir(folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]


class Horse(models.Model):
    name = models.CharField(max_length=100, verbose_name='賽馬娘名稱')
    rarity = models.CharField(max_length=10, choices=[
        ('★1', '★1'), ('★2', '★2'), ('★3', '★3'), 
        ('★4', '★4'), ('★5', '★5')
    ],verbose_name='稀有度')
    distance_type = models.CharField(max_length=20, choices=[
        ('短距離', '短距離'),
        ('一哩', '一哩'),
        ('中距離', '中距離'),
        ('長距離', '長距離'),
    ],verbose_name='距離類型')
    running_style = models.CharField(max_length=20, choices=[
        ('逃げ', '逃げ'),
        ('先行', '先行'),
        ('差し', '差し'),
        ('追込', '追込'),
    ],verbose_name='跑法')
    

    class Meta:
        verbose_name = '馬娘'
        verbose_name_plural = '馬娘'
    def __str__(self):
        return self.name

    def get_image_url(self):
        """回傳靜態圖片的 URL"""
        return f"/static/{self.image_path}"
