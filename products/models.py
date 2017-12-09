from django.db import models

# Create your models here.


class Categorie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    categorie_image = models.ImageField()
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categorie"

    def get_absolute_url(self):
        return reverse('categorie_item_details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, related_name='items')
    description = models.TextField(blank=True)
    price = models.IntegerField()
    item_image = models.ImageField()
    is_available = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name
