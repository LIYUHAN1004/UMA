from django.shortcuts import render

from django.views import View
from django.shortcuts import render, get_object_or_404
from .models.horse import Horse
from .forms import HorseFilterForm

# 顯示馬娘清單
class HorseListView(View):
    def get(self, request):
        horses = Horse.objects.all()
        return render(request, 'uma/horse_list.html', {'horses': horses})

# 顯示馬娘詳細資料
class HorseDetailView(View):
    def get(self, request, pk):
        horse = get_object_or_404(Horse, pk=pk)
        return render(request, 'uma/horse_detail.html', {'horse': horse})

# 篩選功能（用表單）
def horse_filter_view(request):
    form = HorseFilterForm(request.GET or None)
    horses = Horse.objects.prefetch_related('training_results').all()

    if form.is_valid():
        data = form.cleaned_data
        if data.get('distance_type'):
            horses = horses.filter(distance_type=data['distance_type'])
        if data.get('running_style'):
            horses = horses.filter(running_style=data['running_style'])
        if data.get('rarity'):
            horses = horses.filter(rarity=data['rarity'])
        if data.get('min_score'):
            horses = horses.filter(score__gte=data['min_score'])
        if data.get('max_score'):
            horses = horses.filter(score__lte=data['max_score'])

    return render(request, 'uma/horse_filter.html', {'form': form, 'horses': horses})
