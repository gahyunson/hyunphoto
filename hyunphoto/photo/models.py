from django.db import models

class Photo(models.Model):
    photo_path = models.CharField(max_length=200, null=False, blank=False)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=1024)
    size = models.CharField(max_length=15, null=False, blank=False) # 35" x 60"
    price = models.IntegerField(null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'photo'
        verbose_name = 'photo'
        verbose_name_plural = 'photos'


    def __str__(self) -> str:
        return self.title