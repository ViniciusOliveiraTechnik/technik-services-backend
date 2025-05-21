from django.db import models

from .card import Card
from .invoice import Invoice

import uuid

class Purchase(models.Model):

    class Meta:

        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'

    id = models.UUIDField(verbose_name='ID da compra', default=uuid.uuid4, primary_key=True, editable=False)

    card = models.ForeignKey(verbose_name='ID do cartão', to=Card, on_delete=models.CASCADE, related_name='purchases_card')
    invoice = models.ForeignKey(verbose_name='ID da fatura', to=Invoice, on_delete=models.CASCADE, related_name='purchases_invoice')

    purchase_date = models.DateField(verbose_name='Data da compra')
    description = models.CharField(verbose_name='Descrição', default='', max_length=100)
    value = models.DecimalField(verbose_name='Valor', max_digits=10, decimal_places=4)
    installment = models.PositiveIntegerField(verbose_name='Parcela')
    installments = models.PositiveIntegerField(verbose_name='Parcelas')

    def __str__(self):

        return f'{self.description} | R$ {self.value} ({self.card})'