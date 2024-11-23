from django.db import models


class Cart(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False)
    photo = models.ForeignKey('photos.Photo', on_delete=models.DO_NOTHING, null=False)
    price = models.ForeignKey('photos.Price', on_delete=models.DO_NOTHING, null=False)
    quantity = models.IntegerField(default=1, null=False, blank=False)
    is_checked = models.BooleanField(default=True)

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return f"{self.user} - {self.photo} - {self.quantity} pcs"