from django import forms
from.models import  Posts

class BlogForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title','title_tag', 'author','body')

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder':''}),
            'title_tag':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.Select(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'})

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'author','body')

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder':''}),
            'title_tag':forms.TextInput(attrs={'class': 'form-control'}),
            # 'author':forms.Select(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'})

        }