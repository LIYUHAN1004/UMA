from django.db import models
from .horse import Horse


# 支援卡種類（固定 6 種）
SUPPORT_TYPES = [
    ('速度', '速度'),
    ('耐力', '耐力'),
    ('力量', '力量'),
    ('根性', '根性'),
    ('智慧', '智慧'),
    ('友情', '友情'),
]


class SupportCardSet(models.Model):
    """
    一次培育使用的一組支援卡組
    """
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE, related_name='support_sets')
    name = models.CharField(max_length=100, verbose_name='卡組名稱',default='未命名')
    note = models.TextField(blank=True, verbose_name='備註', null=True)

    class Meta:
        verbose_name = '支援卡組'
        verbose_name_plural = '支援卡組'
    def __str__(self):
        return f"{self.name} ({self.horse.name})"


class SupportCard(models.Model):
    """
    單張支援卡
    """
    card_set = models.ForeignKey(SupportCardSet, on_delete=models.CASCADE, related_name='cards')
    card_type = models.CharField(max_length=10, choices=SUPPORT_TYPES, verbose_name='支援卡種類')
    horse_name = models.CharField(max_length=50, verbose_name='馬娘名稱')

    class Meta:
        verbose_name = '支援卡'
        verbose_name_plural = '支援卡'

    def __str__(self):
        return f"{self.card_type}：{self.horse_name}"
