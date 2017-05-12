from django import forms

class CityLocForm(forms.Form):
    city = forms.RegexField(r'',label='City')
MY_CHOICES = (
    ('1', 'Option 1'),
    ('2', 'Option 2'),
    ('3', 'Option 3'),
)
class MyForm(forms.Form):
    my_choice_field = forms.ChoiceField(choices=MY_CHOICES)
	
class WeatherDataForm(forms.Form):
    country = forms.CharField(label="Country")
    city     = forms.CharField(label="City")
    date     = forms.DateTimeField(label="Date")
    temperature = forms.DecimalField(decimal_places=None,
                                     label="Temperature")