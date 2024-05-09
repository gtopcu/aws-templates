

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image_url = models.URLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# python manage.py shell
# from base.models import Item
# items = Item.objects.all()
# print(items)
# Item.objects.create(name='Bread', price=2.50)
# Item.objects.filter(price__gt=2.00)
# Item.objects.get(pk=1)
# Item.objects.all().delete()
# Item.objects.all().update(price=2.50)
# Item.objects.all().update(price=models.F('price') * 2)