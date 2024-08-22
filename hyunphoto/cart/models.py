from django.db import models

class Cart(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING)
    photo = models.ForeignKey('photos.Photo', on_delete=models.DO_NOTHING)
    price = models.ForeignKey('photos.Price', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1, null=False, blank=False)

    class Meta:
        db_table = 'cart'