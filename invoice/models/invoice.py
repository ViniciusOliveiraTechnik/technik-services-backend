from django.db import models

from accounts.models import Account

import uuid

class Invoice(models.Model):

    class Meta:

        verbose_name = 'Fatura'
        verbose_name_plural = 'Faturas'
        indexes = [
            
            models.Index(fields=['account']),
            models.Index(fields=['created_at']),
            models.Index(fields=['purchase_date']),

        ]

    id = models.UUIDField(verbose_name='ID Fatura', primary_key=True, default=uuid.uuid4, unique=True, null=False, editable=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='invoices')

    card = models.CharField(verbose_name='Nome no cartão',  max_length=50, default='', blank=True, null=True)
    purchase_date = models.DateTimeField(verbose_name='Data de compra')
    description = models.TextField(verbose_name='Descrição', default='', blank=True, null=True)
    value = models.DecimalField(verbose_name='Valor', max_digits=10, decimal_places=2, default=0.00)
    installment = models.IntegerField(verbose_name='Parcela', default=1)
    installments = models.IntegerField(verbose_name='Parcelas', default=1)

    created_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='created_invoices')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):

        return f'{self.account.first_name} {self.account.last_name } - {self.purchase_date} - R$ {self.value}'