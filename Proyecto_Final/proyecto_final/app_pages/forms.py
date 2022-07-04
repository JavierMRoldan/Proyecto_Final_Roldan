from django import forms


class Blog_formulario(forms.Form):

    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=50)
    cuerpo = forms.CharField(max_length=100)
    autor = forms.CharField(max_length=50)
    fecha = forms.DateField()