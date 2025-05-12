from django.db import models
import uuid

from accounts.models import Account

class Card(models.Model):

    class Meta:

        verbose_name = 'Cartão'
        verbose_name_plural = 'Cartões'

    class BankOptions(models.TextChoices):

        ITAU = 'Itaú'
        BB = 'Banco do Brasil'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField('Data de crição', auto_now_add=True)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField('Nome do cartão', max_length=150, unique=True, blank=False, null=False)
    bank = models.CharField('Banco', choices=BankOptions.choices, max_length=20, default='')
    is_active = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return f'{self.name} - {self.bank}'