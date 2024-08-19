from django import forms

from .models import Luggage


class LuggageForm(forms.ModelForm):
    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False
    )

    class Meta:
        model = Luggage
        fields = ['storage_time', 'luggage_name', 'luggage_size', 'luggage_description', 'images']
        widgets = {
            'storage_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'luggage_name': forms.TextInput(attrs={'placeholder': '请输入行李名称'}),
            'luggage_size': forms.TextInput(attrs={'placeholder': '请输入行李规格'}),
            'luggage_description': forms.Textarea(attrs={'placeholder': '请输入行李描述'}),
        }
