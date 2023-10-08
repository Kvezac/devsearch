from django.forms import ModelForm
from .models import Project, Review
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'value']

        labels = {
            'body': 'Add a comment to your vote',
            'value': 'Place your vote'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['owner', 'vote_ratio', 'vote_total', 'created']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'input'})
