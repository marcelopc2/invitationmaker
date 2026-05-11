from django import forms
from django.forms import inlineformset_factory
from .models import Invitacion, CapaParallax

class InvitacionForm(forms.ModelForm):
    class Meta:
        model = Invitacion
        fields = [
            'titulo_landing', 'slug', 'descripcion', 'fecha_evento', 
            'direccion_texto', 'direccion_google_maps_link', 'link_lista_deseos',
            'color_primario', 'color_texto', 'fuente_texto',
            'fuerza_giro', 'fuerza_desplazamiento', 'activar_bokeh'
        ]
        widgets = {
            'titulo_landing': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: ¡Bienvenido Mateo!'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: baby-shower-mateo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Texto de bienvenida o dedicatoria...'}),
            'fecha_evento': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'direccion_texto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Calle Falsa 123, Ciudad'}),
            'direccion_google_maps_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://maps.google.com/...'}),
            'link_lista_deseos': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://amazon.com/...'}),
            'color_primario': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color w-100', 'title': 'Elige el color principal'}),
            'color_texto': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color w-100', 'title': 'Elige el color del texto'}),
            'fuente_texto': forms.Select(attrs={'class': 'form-select'}),
            'fuerza_giro': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'fuerza_desplazamiento': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'activar_bokeh': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

CapaParallaxFormSet = inlineformset_factory(
    Invitacion, 
    CapaParallax, 
    fields=['imagen', 'z_index', 'orden', 'dispositivo', 'pegar_abajo'], 
    extra=0, 
    can_delete=True,
    widgets={
        'imagen': forms.FileInput(attrs={'class': 'form-control form-control-sm'}),
        'z_index': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Ej: -5, 0, 5'}),
        'orden': forms.NumberInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Orden visual'}),
        'dispositivo': forms.Select(attrs={'class': 'form-select form-select-sm'}),
        'pegar_abajo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }
)
