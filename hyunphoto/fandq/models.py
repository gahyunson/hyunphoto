from django.db import models

class Fandq(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=1024)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'fandq'
        verbose_name = 'fandq'
        verbose_name_plural = 'fandqs'
    
class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, null=False, blank=False)

    class Meta:
        db_table = 'fandq_category'

    def __str__(self) -> str:
        return self.name
