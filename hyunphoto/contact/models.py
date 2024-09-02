from django.db import models

class Contact(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    message = models.TextField(max_length=1024, null=False, blank=False)

    class Meta:
        db_table = 'contact'