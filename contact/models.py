from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    subject = models.CharField(max_length=45)
    message = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact Messages'
