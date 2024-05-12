from django import forms
from django.core.validators import RegexValidator
from .models import Personas, Avisitantes

class SearchForm(forms.Form):
        dni = forms.CharField(
        label='',
        max_length=10,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escriba el numero de Identificación'
        })
    )
class PersonForms(forms.ModelForm):
    dni_validator = RegexValidator(r'^\d{6,10}$', 'Ingrese solo números válidos con un mínimo de 6 dígitos.')
    name_validator = RegexValidator(r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$', 'Ingrese solo letras válidas para el nombre.')
    class Meta:
        model = Personas
        fields = ['nac', 'dni', 'first_name', 'last_name', 'gender','status']
        widgets = {
            'nac': forms.Select(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dni'].validators.append(self.dni_validator)
        self.fields['first_name'].validators.append(self.name_validator)
        self.fields['last_name'].validators.append(self.name_validator)

        # Deshabilitar los campos Dni y photo si ya existe una instancia
        if self.instance.pk:
            self.fields['dni'].disabled = True
          
    # Sobrescribe el método clean para mostrar errores personalizados
    def clean(self):
        cleaned_data = super().clean()
        dni = cleaned_data.get('dni')
        if dni and not dni.isdigit():
            self.add_error('dni', 'Ingrese solo números válidos con un mínimo de 6 dígitos.')
        return cleaned_data
    
    def save(self, commit=True):
        # Guardar la instancia
        person =super().save(commit=False)
        if commit:
            first_name = person.first_name
            last_name = person.last_name
            person.first_name = first_name.capitalize()
            person.last_name = last_name.capitalize()
            person.save()
        return person

class AccessForms(forms.ModelForm):
    class Meta:
        model = Avisitantes
        fields = ['entry','hours','hoursEx', 'empleado', 'oficina','obs']
        widgets = {
            'entry': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'hours': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hoursEx': forms.TimeInput(attrs={'type': 'time','class': 'form-control'}),
            'empleado': forms.Select(attrs={'class': 'form-control'}),
            'oficina': forms.Select(attrs={'class': 'form-control'}),
            'obs': forms.Textarea(attrs={'class': 'form-control'}),
           
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.id:  # Si el objeto ya existe
            self.fields['entry'].widget = forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
            self.fields['entry'].widget.attrs['readonly'] = True 
            self.fields['hours'].widget.attrs['readonly'] = True 
            self.fields['empleado'].widget.attrs['readonly'] = True 
            self.fields['oficina'].widget.attrs['readonly'] = True 
    
    def clean(self):
        cleaned_data = super().clean()
        if self.instance.id:
            if cleaned_data['entry']!=self.instance.entry:
                raise forms.ValidationError('No se permite modificar la Fecha')
            if cleaned_data['hours']!=self.instance.hours:
                raise forms.ValidationError('No se permite modificar la hora de Entrada')

        return cleaned_data
       

                                                                                                                                                  