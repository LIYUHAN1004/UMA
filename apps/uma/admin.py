from django.contrib import admin
from django.utils.html import format_html
from .models import Horse, TrainingResult, SupportCardSet, SupportCard


class SupportCardInline(admin.TabularInline):
    model = SupportCard
    extra = 6  # 預設顯示 6 張卡
    max_num = 6  # 限制最多 6 張


@admin.register(SupportCardSet)
class SupportCardSetAdmin(admin.ModelAdmin):
    list_display = ('name', 'horse', 'note')
    inlines = [SupportCardInline]


@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'distance_type', 'running_style')
    



@admin.register(TrainingResult)
class TrainingResultAdmin(admin.ModelAdmin):
    list_display = ('horse', 'date', 'evaluation_score')


@admin.register(SupportCard)
class SupportCardAdmin(admin.ModelAdmin):
    list_display = ('card_set', 'card_type', 'horse_name')
    

