from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"
        db_table = "emails"

    def __str__(self):
        return self.email