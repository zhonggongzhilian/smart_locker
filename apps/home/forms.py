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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        luggage = super().save(commit=False)
        if commit:
            luggage.user = self.user
            luggage.save()
            self.save_m2m()
        return luggage
