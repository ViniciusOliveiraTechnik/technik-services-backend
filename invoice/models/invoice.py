from django.db import models

import uuid

class Invoice(models.Model):
    
    class BankChoices(models.TextChoices):

        ITAU = 'Itaú'
        BANCO_DO_BRASIL = 'Banco do Brasil'

    class Meta:

        verbose_name = 'Fatura'
        verbose_name_plural = 'Faturas'
        constraints = [
            models.UniqueConstraint(fields=['bank', 'invoice_date'], name='unique_bank_invoice_date')
        ]

    id = models.UUIDField(verbose_name='ID da fatura', default=uuid.uuid4, primary_key=True, editable=False, null=False, blank=False)

    invoice_date = models.DateField(verbose_name='Data da fatura', unique=True)
    bank = models.CharField(verbose_name='Banco', choices=BankChoices.choices)

    def __str__(self):
        
        return f'Fatura ( {self.invoice_date} | {self.bank} )'