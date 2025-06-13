from django.db import models

import uuid

from accounts.models import Account

class OneTimeCode(models.Model):

    class Meta:

        verbose_name = 'Código de Tempo Único'
        verbose_name_plural = 'Códigos de Tempos Únicos'
        constraints = [
            models.UniqueConstraint(fields=['account', 'code'], name='unique_account_code')
        ]

    id = models.UUIDField(verbose_name='ID do Código', primary_key=True, editable=False,  default=uuid.uuid4)
    account = models.ForeignKey(verbose_name='ID do Usário', to=Account, on_delete=models.CASCADE, related_name='account_otp_codes')
    is_used = models.BooleanField(verbose_name='Usado', default=False)
    code = models.BinaryField(verbose_name='Código')