from django import forms
#from django.contrib.auth.models import User
from users.models import User
import django.forms
import django.forms.utils
import django.forms.widgets

class RegisterForm(forms.Form):
    nombre = forms.CharField(min_length=3 ,max_length=30, required=True, widget=forms.TextInput(attrs={
        'name':'nombre',
        'id':'inputNombre',
        'class':'input-text', 
        'placeholder':'' ,
        'autofocus':'',

        'autocomplete': 'given-name',
        'type': 'text',
        'value': ''
    }))
    # id="billing_first_name" name="billing_first_name"
    apellidos = forms.CharField(min_length=3, max_length=30, required=True, widget=forms.TextInput(attrs={
        'name':'apellidos',
        'id':'inputApellidos',
        'class':'input-text', 
        'placeholder':'' ,
        'autofocus':'',

        'autocomplete': 'family-name',
        'type': 'text',
        'value': ''
    }))
    # id="billing_last_name" name="billing_last_name"
    compania = forms.CharField(min_length=1, max_length=30, required=False, widget=forms.TextInput(attrs={
        'name':'compania',
        'id':'inputCompania',
        'class':'input-text', 
        'placeholder':'' ,
        'autofocus':'',

        'type':'text',
         'value':''
    }))
    #id="billing_company" name="billing_company"  
    e_mail = forms.EmailField(min_length=1, max_length=50,required=True, widget=forms.EmailInput(attrs={
        'type': 'email',
        'name':'email',
        'id':'inputEmail',
        'class':'input-text', 
        'placeholder':'email@ejemplo.com' ,
        'autofocus':'',

        'autocomplete': 'email',
        'value': ''
    }))
    # id="billing_email" name="billing_email" 
    telefono = forms.CharField(min_length=10, max_length=10, required=True, widget=forms.TextInput(attrs={
        'type': 'tel',
        'name':'telefono',
        'id':'inputPhone',
        'class':'input-text', 
        'placeholder':' 10 dígitos' ,
        'required':'',
        'autofocus':'',

        'value':''
    }))
    # id="billing_phone" name="billing_phone"
    direccion = forms.CharField(min_length=1, max_length=40, required=True, widget=forms.TextInput(attrs={
        'name':'direccion',
        'id':'inputDireccion',
        'class':'input-text', 
        'placeholder':'Calle y número' ,
        'autofocus':'',

        'autocomplete':'address-line1',
        'type': 'text',
        'value': ''
    }))
    # id="billing_address_1" name="billing_address_1"
    colonia = forms.CharField(min_length=1, max_length=30, required=True, widget=forms.TextInput(attrs={
        'name':'colonia',
        'id':'inputColonia',
        'class':'input-text', 
        'placeholder':'' ,
        'autofocus':'',

        'autocomplete':'address-line2',
        'type': 'text',
        'value': ''
    }))
    #id="billing_address_2" name="billing_address_2"
    ciudad = forms.CharField(min_length=1, max_length=30, required=True, widget=forms.TextInput(attrs={
        'name':'ciudad',
        'id':'inputaCiudad',
        'class':'input-text', 
        'placeholder':'' ,
        'autofocus':'',

        'autocomplete': 'address-level2',
        'type': 'text',
        'value': ''
    }))
    #id="billing_city" name="billing_city"
    listaEstados= [
        ('', 'Selecciona un estado'),
        ('Aguascalientes','Aguascalientes'),
        ('BajaCalifornia','Baja California'),
        ('BajaCaliforniaSur','Baja California Sur'),
        ('Campeche','Campeche'),
        ('Chihuahua','Chihuahua'),
        ('Chiapas','Chiapas'),
        ('Coahuila','Coahuila'),
        ('Colima','Colima'),
        ('Durango','Durango'),
        ('Guanajuato','Guanajuato'),
        ('Guerrero','Guerrero'),
        ('Hidalgo','Hidalgo'),
        ('Jalisco','Jalisco'),
        ('EdoMexico','Estado de México'),
        ('Michoacan','Michoacán'),
        ('Morelos','Morelos'),
        ('Nayarit','Nayarit'),
        ('NuevoLeon','Nuevo León'),
        ('Oaxaca','Oaxaca'),
        ('Puebla','Puebla'),
        ('Queretaro','Querétaro'),
        ('QuintanaRoo','Quintana Roo'),
        ('SanLuisPotosi','San Luis Potosí'),
        ('Sinaloa ','Sinaloa '),
        ('Sonora','Sonora'),
        ('Tabasco','Tabasco'),
        ('Tamaulipas','Tamaulipas'),
        ('Tlaxcala','Tlaxcala'),
        ('Veracruz','Veracruz'),
        ('Yucatan','Yucatán'),
        ('Zacatecas','Zacatecas'),
        ('CDMX','Ciudad de México')
        #value, label
    ]
    estado = forms.ChoiceField(choices=listaEstados, required=True, widget=forms.Select(attrs={
        'name':'estado',
        'class': 'country_to_state country_select'
    }))
    codigoPostal = forms.CharField(min_length=5, max_length=5, required=True, widget=forms.TextInput(attrs={
        'name':'codigopostal',
        'id':'inputCodigoPostal',
        'class':'input-text', 
        'placeholder':'' ,
        'autofocus':''
    }))

    password = forms.CharField( min_length=6 ,max_length=30, required=True, widget=forms.PasswordInput({
        'type': 'password',
        'name': 'password',
        'id': 'inputPassword',
        'class': 'input-text',
        'placeholder': '',
        'autocomplete': 'off'
    }))
    passwordCopy = forms.CharField( min_length=6 ,max_length=30, required=True, widget=forms.PasswordInput({
        'type': 'password',
        'name': 'password2',
        'id': 'inputNewPassword2',
        'class': 'input-text',
        'placeholder': '',
        'autocomplete': 'off'
    }))
    

    def clean_username(self):
        username = self.cleaned_data.get('email')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Este correo electrónico ya se encuentra registrado')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya se encuentra registrado')
        return email

    

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('passwordCopy') != cleaned_data.get('password'):
            self.add_error('passwordCopy', 'La contraseña no coincide')

    def save(self):
        return User.objects.create_user(
                self.cleaned_data.get('e_mail'), #usr
                self.cleaned_data.get('e_mail'),
                self.cleaned_data.get('password'),
                first_name = self.cleaned_data.get('nombre'),
                last_name = self.cleaned_data.get('apellidos'),
                telefono = self.cleaned_data.get('telefono'),
                compania = self.cleaned_data.get('compania'),
                direccion =self.cleaned_data.get('direccion'),
                colonia = self.cleaned_data.get('colonia'),
                ciudad = self.cleaned_data.get('ciudad'),
                estado = self.cleaned_data.get('estado'),
                codigoPostal = self.cleaned_data.get('codigoPostal'),
            )
        

class LoginForm(forms.Form):
    e_mail = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'type': 'email',
        'name':'email',
        'id':'inputEmail',
        'class':'input-text', 
        'placeholder':'E-mail' ,
        'autofocus':'',
        'autocomplete': 'email',
        'value': ''
    }))
    password = forms.CharField(min_length=6 ,max_length=30, required=True, widget=forms.PasswordInput({
        'type': 'password',
        'name': 'password',
        'id': 'inputPassword',
        'class': 'input-text',
        'placeholder': 'Contraseña',
        'autocomplete': 'off'
    }))
    
class ConsultaFechaForm(forms.Form):
    fecha = forms.DateField(
        label='fecha',
        widget=django.forms.DateInput(
            format='%Y-%m-%d',
            attrs={'placeholder': 'dd/mm/aaaa', 'class': 'date', 'type': 'date'}))
    

    
