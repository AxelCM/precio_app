from django.db import models
from django.conf import settings
from crum import get_current_user
from datetime import datetime

class DataControl(models.Model):
    user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, blank=True, related_name='%(app_label)s_%(class)s_creation')
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_updated = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='%(app_label)s_%(class)s_updated' )
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract =  True


class TypeSize(DataControl):
    name = models.CharField('Nombre' , max_length=100)
    unit = models.CharField('Unidad' , max_length=10)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(TypeSize, self).save()

class Size(DataControl):
    type = models.ForeignKey(TypeSize, on_delete=models.CASCADE)
    name = models.CharField('Nombre' , max_length=100)
    vertical = models.IntegerField('Medida Vertical' ,)
    horizontal = models.IntegerField('Medida Horizontal')
    title  = models.IntegerField('Tam. Titulo' , default=24)
    description  = models.IntegerField('Tam. Descripcion' , default=12)
    price = models.IntegerField('Tam. Precio' , default=12)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Size, self).save()

class Season(DataControl):
    name = models.CharField('Nombre' , max_length=100)
    background = models.ImageField(
    'Fondo',
    upload_to = 'productos/images',
    blank= True,
    null = True
    )

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Season, self).save()

class Product(DataControl):
    upc = models.CharField('UPC' , max_length=50 , default=0)
    name = models.CharField('Nombre' , max_length=100)
    description = models.TextField('Descripcion' , blank=True , null=True )
    price = models.DecimalField('Precio Oferta',max_digits=10, decimal_places=2, default=0)
    price_normal = models.DecimalField('Precio Normal',max_digits=10, decimal_places=2, default=0)
    stock = models.IntegerField('Existencia' , default=0 , blank=True , null=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Product, self).save()

class Pricer(DataControl):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    cant = models.IntegerField('Cantidad' , default=1 , blank=True , null=True)

    def __str__(self):
        return "{} {}".format(self.season, self.product.name)

    def product_data(self):
        return "{} Q.{}".format(self.product.name , self.product.price)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Pricer, self).save()

class Computer(DataControl):
    upc = models.CharField('UPC' , max_length=50 , default=0)
    model = models.CharField('Modelo' , max_length=100)
    cpu = models.CharField('Procesador' , max_length=100 , blank=True , null=True)
    gpu = models.CharField('Tarjeta Grafica' , max_length=100 , blank=True , null=True)
    ram = models.IntegerField('Memoria RAM' , default=1 , blank=True , null=True)
    hdd = models.CharField('HDD' , max_length=100, blank=True, null=True)
    ssd = models.CharField('SSD' , max_length=100, blank=True, null=True)
    screen = models.CharField('Pantalla' , max_length=100)
    hz = models.CharField('Frecuenta de pantalla' , max_length=100, blank=True, null=True)
    system = models.CharField('S.O' , max_length=100, blank=True, null=True)
    other = models.CharField('Adicionales' , max_length=250, blank=True, null=True)
    normal_price = models.DecimalField('Precio Normal',max_digits=10, decimal_places=2, default=0)
    ofert_price = models.DecimalField('Precio de Oferta',max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return "{} {} {} {}".format(self.model, self.ram, self.hdd, self.ssd)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Computer, self).save()

class ComputerPricer(DataControl):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    cant = models.IntegerField('Cantidad' , default=1 , blank=True , null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(ComputerPricer, self).save()
