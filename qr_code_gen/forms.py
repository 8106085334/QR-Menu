from django import forms 


class QR_Code_Form(forms.Form):
    resturant_name = forms.CharField(
        max_length=50,
        label="Restuarnat Name",
        widget = forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Restaurant Name',
          })
        )
    url = forms.URLField(
        max_length=250,
        label="Menu Url",
        widget = forms.URLInput(attrs={
            'class':'form-control',
            'placeholder':'Enter Restuarant Url'
        })
        )
