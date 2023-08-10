from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=256)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(name)


