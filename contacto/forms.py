from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre' ,required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=25)
    email = forms.EmailField( label='Email' ,required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu email'}
    ), min_length=3, max_length=25)
    content = forms.CharField(label='Mensaje' ,required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows':5, 'placeholder':'Escribe tu mensaje'}
    ))