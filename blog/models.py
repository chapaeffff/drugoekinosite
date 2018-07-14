from django.db import models
from django.template.defaultfilters import slugify
from transliterate import translit

from filmbase.models import *

class List(models.Model):
    title = models.CharField(max_length = 400)
    intro = models.TextField()
    slug = models.SlugField(max_length=60, blank=True)

    def save(self, *args, **kwargs):
        # if not self.id:
            #Only set the slug when the object is created.
        self.slug = slugify(translit(self.title,'ru', reversed=True)) #Or whatever you want the slug to use
        super(List, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog.views.list_pk', args=[str(self.slug)])

    def __str__(self):
        return self.title



class Film_List_Elem(models.Model):
    film = models.ForeignKey('filmbase.Film', on_delete=models.PROTECT)
    text = models.TextField()
    order = models.IntegerField()
    owner_list = models.ForeignKey('List',  on_delete=models.PROTECT, null = True, blank = True, default = 1)

    def __str__(self):
        return self.film.title