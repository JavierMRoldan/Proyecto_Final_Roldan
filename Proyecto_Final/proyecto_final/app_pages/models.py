from django.db import models
from django.db.models.signals import pre_save
from proyecto_final.utils import unique_slug_generator
# Create your models here.
class Blogs(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    fecha = models.DateField()
    slug = models.SlugField(max_length=200, null=True, blank=True)

def slug_generator(sender, instance, *args , **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Blogs)


