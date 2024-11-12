from django.utils import timezone
from django.db import models
from datetime import timedelta
from django.core.validators import MinLengthValidator
class ApiAluno(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)], verbose_name='nome')
    lastname = models.CharField(max_length=100, verbose_name='sobrenome')
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        if not self.expiration_date:
            self.expiration_date = self.created_at + timedelta(days=31)
        super(ApiAluno, self).save(*args, **kwargs)