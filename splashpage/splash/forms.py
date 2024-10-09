from django import forms

class ProspectForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()       
    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder':'Your name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder':'Your email address'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder':'What questions do you have?'})

class QuickProspectForm(forms.Form):
    email = forms.EmailField()       

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder':'Your email'})
