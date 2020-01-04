from django import forms
class Car_testing(forms.Form):
    color = forms.CharField()
    year = forms.IntegerField()
    manufacturer = forms.CharField()
    required_css_class = "field"
    error_css_class = "error"