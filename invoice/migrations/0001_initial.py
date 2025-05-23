# Generated by Django 5.1.7 on 2025-05-19 12:16

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID da fatura')),
                ('invoice_date', models.DateField(unique=True, verbose_name='Data da fatura')),
            ],
            options={
                'verbose_name': 'Fatura',
                'verbose_name_plural': 'Faturas',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID do cartão')),
                ('name', models.CharField(default='', max_length=20, verbose_name='Nome no cartão')),
                ('bank', models.TextField(choices=[('Itaú', 'Itau'), ('Banco do Brasil', 'Banco Do Brasil')], default='Itaú', verbose_name='Banco do cartão')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to=settings.AUTH_USER_MODEL, verbose_name='ID do usuário')),
            ],
            options={
                'verbose_name': 'Cartão',
                'verbose_name_plural': 'Cartões',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID da compra')),
                ('purchase_date', models.DateTimeField(auto_now_add=True, verbose_name='Data da compra')),
                ('description', models.CharField(default='', max_length=100, verbose_name='Descrição')),
                ('value', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Valor')),
                ('installment', models.PositiveIntegerField(verbose_name='Parcela')),
                ('installments', models.PositiveIntegerField(verbose_name='Parcelas')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_card', to='invoice.card', verbose_name='ID do cartão')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_invoice', to='invoice.invoice', verbose_name='ID da fatura')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.AddConstraint(
            model_name='card',
            constraint=models.UniqueConstraint(fields=('account', 'name', 'bank'), name='unique_account_name_bank'),
        ),
        migrations.AddConstraint(
            model_name='purchase',
            constraint=models.UniqueConstraint(fields=('card', 'purchase_date', 'description', 'installment'), name='unique_card_purchase_date_description_installment'),
        ),
    ]
