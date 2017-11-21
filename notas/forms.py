from django import forms
from .models import Grado, Curso, Pensum

class GradoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Grado
        fields = ('nombre','seccion', 'cursos')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.
#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.
    def __init__ (self, *args, **kwargs):
        super(GradoForm, self).__init__(*args, **kwargs)
#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["cursos"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["cursos"].help_text = "Ingrese los Cursos "
        self.fields["cursos"].queryset = Curso.objects.all()
