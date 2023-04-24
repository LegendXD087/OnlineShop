from django.db import models


class AddUser(models.Model):
    title = models.CharField('First Name', max_length=128)
    name = models.CharField('Last Name', max_length=128)
    phone = models.CharField('Phone Number', max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
