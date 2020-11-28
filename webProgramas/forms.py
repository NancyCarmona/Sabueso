from django import forms

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
    email = forms.EmailField( required=True, widget=forms.EmailInput(attrs={
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
        'name':'phonenumber',
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
    listaEstados= (
        ('Selecciona estado', ''),
        ('Aguascalientes','Aguascalientes'),
        ('Baja California','Baja California'),
        ('Baja California Sur','Baja California Sur'),
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
        ('Edo. de México','EdoMéxico'),
        ('Michoacán','Michoacán'),
        ('Morelos','Morelos'),
        ('Nayarit','Nayarit'),
        ('Nuevo León','Nuevo León'),
        ('Oaxaca','Oaxaca'),
        ('Puebla','Puebla'),
        ('Querétaro','Querétaro'),
        ('Quintana Roo','Quintana Roo'),
        ('San Luis Potosí','San Luis Potosí'),
        ('Sinaloa ','Sinaloa '),
        ('Sonora','Sonora'),
        ('Tabasco','Tabasco'),
        ('Tamaulipas','Tamaulipas'),
        ('Tlaxcala','Tlaxcala'),
        ('Veracruz','Veracruz'),
        ('Yucatán:','Yucatán:'),
        ('Zacatecas','Zacatecas'),
        ('Ciudad de México','Ciudad de México')
    )
    estado = forms.ChoiceField(choices=listaEstados, required=True, widget=forms.TextInput(attrs={
        'name':'estado',
        'id':'inputEstado',
        'class':'input-text', 
        'placeholder':'' ,
        'autofocus':''
    }))
    codigoPostal = forms.CharField(min_length=1, max_length=30, required=True, widget=forms.TextInput(attrs={
        'name':'codigopostal',
        'id':'inputCodigoPostal',
        'class':'input-text', 
        'placeholder':'' ,
        'autofocus':''
    }))

    password = forms.CharField( min_length=6 ,max_length=30, required=True, widget=forms.PasswordInput({
        'type': 'password',
        'name': 'password',
        'id': 'inputNewPassword',
        'data-error-threshold': '50',
        'data-warning-threshold': '75',
        'class': 'field',
        'placeholder': 'Contraseña',
        'autocomplete': 'off'
    }))
    passwordCopy = forms.CharField( min_length=6 ,max_length=30, required=True, widget=forms.PasswordInput({
        'type': 'password',
        'name': 'password2',
        'id': 'inputNewPassword2',
        'class': 'field',
        'placeholder': 'Confirmar contraseña',
        'autocomplete': 'off'
    }))