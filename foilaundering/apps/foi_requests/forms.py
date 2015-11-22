from django import forms

from .models import FOIRequest


class ArticleForm(forms.ModelForm):
    class Meta:
        model = FOIRequest
        fields = ['foi_text', 'receiving_authority',]
        widgets = {
            'foi_text': forms.Textarea(attrs={'rows':15, 'cols':15}),
        }
