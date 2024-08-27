from django import forms
from posts.models import Post, Tag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'title', 'content', 'rate']
        widgets = {
            'image': forms.ClearableFileInput(
                attrs={
                    'multiple': False,
                    'placeholder': 'Upload image',
                    'rows': 10,
                    'cols': 20
                }),
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                    'rows': 10,
                    'cols': 20
                }),
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Content',
                    'rows': 10,
                    'cols': 20
                }),
            'rate': forms.NumberInput(
                attrs={
                    'placeholder': 'Rate',
                    'rows': 10,
                    'cols': 20
                })
        }


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=50,
        min_length=1,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search',
                'class': 'form-control',
            }))
    tags = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    orderings = (
        ('title', 'по заголовку'),
        ('-title', 'по заголовку в обратном порядке'),
        ('rate', 'по рейтингу'),
        ('-rate', 'по рейтингу в обратном порядке'),

    )
    orderings = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(attrs={'placeholder': 'Ordering', 'class': 'form-control'})
    )
