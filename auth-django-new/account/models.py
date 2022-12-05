from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200, null=True)
    birthdate = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    is_active = models.CharField(max_length=200, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

