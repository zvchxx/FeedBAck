from django import forms
from feedback.models import OfferModel, ProblemModel


class OfferForm(forms.ModelForm):
    class Meta:
        model = OfferModel
        fields = ['title', 'description']


class ProblemForm(forms.ModelForm):
    class Meta:
        model = ProblemModel
        fields = ['title', 'description']