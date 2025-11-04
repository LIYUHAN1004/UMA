from django import forms

class HorseFilterForm(forms.Form):
    
    distance_type = forms.ChoiceField(
        choices=[('', '不指定'), ('短距離', '短距離'), ('一哩', '一哩'), ('中距離', '中距離'), ('長距離', '長距離')],
        required=False,
        label='距離類型'
    )
    running_style = forms.ChoiceField(
        choices=[('', '不指定'), ('逃げ', '逃げ'), ('先行', '先行'), ('差し', '差し'), ('追込', '追込')],
        required=False,
        label='跑法'
    )
    rarity = forms.ChoiceField(
        choices=[('', '不指定'), ('★1', '★1'), ('★2', '★2'), ('★3', '★3'), ('★4', '★4'), ('★5', '★5')],
        required=False,
        label='星級'
    )
    min_score = forms.IntegerField(required=False, label='最低分數')
