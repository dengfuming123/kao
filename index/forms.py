from django import forms

class SelectCategory(forms.Form):
    Article_category = (
        ('科技', '科技'),
        ('游戏', '游戏'),
        ('影视', '影视'),
        ('其它', '其它'),
    )
    category = forms.CharField(max_length=20, widget=forms.Select(choices=Article_category))