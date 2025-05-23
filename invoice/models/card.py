from accounts.models import Account

from django.db import models

import uuid

class Card(models.Model):

    class Meta:

        verbose_name = 'Cartão'
        verbose_name_plural = 'Cartões' 
        constraints = [
            models.UniqueConstraint(fields=['account', 'name', 'bank'], name='unique_account_name_bank')
        ]

    class BankChoices(models.TextChoices):

        ITAU = 'Itaú'
        BANCO_DO_BRASIL = 'Banco do Brasil'

    id = models.UUIDField(verbose_name='ID do cartão', default=uuid.uuid4, primary_key=True, editable=False)

    account = models.ForeignKey(verbose_name='ID do usuário', to=Account, on_delete=models.CASCADE, related_name='cards')

    name = models.CharField(verbose_name='Nome no cartão', default='', max_length=50)
    bank = models.TextField(verbose_name='Banco do cartão', choices=BankChoices.choices, default=BankChoices.ITAU)

    def __str__(self):

        return f'{self.name} ({self.bank})'
