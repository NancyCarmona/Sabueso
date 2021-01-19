from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.core.validators import RegexValidator
from webProgramas.settings import MEDIA_URL, STATIC_URL

class User(AbstractUser):
    #imagen = models.ImageField(upload_to='media/ProfilePic/%Y/%m/%d', height_field=None, width_field=None, max_length=None, null=True, blank=True)
    telefono = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    compania = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=17)
    codigoPostal = models.CharField(max_length=5, validators=[RegexValidator(r'^\d{1,10}$')])
    tipoUsuario = models.CharField(max_length=45, default='basico')
    tipoCuenta = models.CharField(max_length=45, default='basico')
    intereses = models.CharField(max_length=45, blank=True, null=True)

    #video 42 algorisoft para poner imagen de perfil
    def getImagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'images/empty.png')

class Alerta(models.Model):
    idAlerta = models.AutoField(primary_key=True)
    nombreAlerta = models.CharField(max_length=50)
    idUsuario = models.ForeignKey("users.User", on_delete=models.CASCADE)
    palabrasClave = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    subcategoria = models.CharField(max_length=50)
    fechaCreacion = models.DateField(auto_now=False, auto_now_add=True)
    fechaBorrada = models.DateField()
    statusAlerta = models.CharField(max_length=50)
    precision = models.CharField(max_length=50)

class BitacoraEnvio(models.Model):
    idBitacora = models.AutoField( primary_key=True)
    statusBitacora = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    nombreAlerta = models.CharField(max_length=50)
    idUsuarios = models.ForeignKey("users.User", on_delete=models.CASCADE) # 2 foreign key? ok
    bitacoraEnvioCol = models.CharField(max_length=50)
    idAlerta = models.ForeignKey("users.Alerta", on_delete=models.CASCADE)

    class Meta:
        pass
        #verbose_name = _("BitacoraEnvio")
        #verbose_name_plural = _("BitacoraEnvios")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("BitacoraEnvio_detail", kwargs={"pk": self.pk})

class AlertaHasContenido(models.Model):
    idAlertaContenido = models.ForeignKey("users.Alerta", on_delete=models.CASCADE)
    idContenido = models.ForeignKey("users.Contenido", on_delete=models.CASCADE)
    notificado = models.CharField(max_length=50)
    alertaHasContenidocol = models.CharField(max_length=50)

    class Meta:
        pass
        #verbose_name = _("AlertaHasContenido")
        #verbose_name_plural = _("AlertaHasContenidos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("AlertaHasContenido_detail", kwargs={"pk": self.pk})

class Contenido(models.Model):
    idContenido = models.AutoField(primary_key=True)
    cont = models.CharField(max_length=50)

    class Meta:
        pass
        #verbose_name = _("Contenido")
        #verbose_name_plural = _("Contenidos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Contenido_detail", kwargs={"pk": self.pk})

class DescargaNotaDOF(models.Model):
    idDescargaNotaDOF = models.AutoField(primary_key=True)
    codNota = models.CharField(max_length=50)
    titulo = models.TextField( null=True, blank=True)
    codOrga1 = models.CharField(max_length=50)
    codOrga2 = models.CharField(max_length=50)
    pagina = models.CharField(max_length=50)
    codSeccion = models.CharField(max_length=50)
    existePDF = models.CharField(max_length=50, null=True, blank=True)
    fecha = models.CharField(max_length=50)

    #FULLTEXT KEY `titulo` (`titulo`),
    #FULLTEXT KEY `titulo_2` (`titulo`)
    

    class Meta:
        pass
        #verbose_name = _("DescargaNotaDOF")
        #verbose_name_plural = _("DescargaNotaDOFs")

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("DescargaNotaDOF_detail", kwargs={"pk": self.pk})

class Secretaria(models.Model):
    idSecretaria = models.AutoField(primary_key=True)
    nombreSecretaria = models.CharField(max_length=50)
    tipoSecretaria = models.CharField(max_length=50)
    estadoSecretaria = models.CharField(max_length=50)
    

    class Meta:
        pass
        #verbose_name = _("Secretaria")
        #verbose_name_plural = _("Secretarias")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Secretaria_detail", kwargs={"pk": self.pk})

class AvisoSitio(models.Model):
    idAvisos = models.AutoField(primary_key=True)
    textoAviso = models.CharField(max_length=50)
    statusAviso = models.CharField(max_length=50)
    usuario = models.ForeignKey("users.User", on_delete=models.CASCADE)
    

    class Meta:
        pass
        #verbose_name = _("AvisosSitio")
        #verbose_name_plural = _("AvisosSitios")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("AvisosSitio_detail", kwargs={"pk": self.pk})


class Pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    tipoPago = models.CharField(max_length=50)
    banco = models.CharField(max_length=50)
    usuario = models.ForeignKey("users.User", on_delete=models.CASCADE)

    class Meta:
        pass
        #verbose_name = _("Pago")
        #verbose_name_plural = _("Pagos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Pago_detail", kwargs={"pk": self.pk})




