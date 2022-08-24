# Generated by Django 3.2.13 on 2022-08-24 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_currencyalteration_rateofexchange_voucher_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_name',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='company_alt_currency',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='cost_centre',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='currencyalteration',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='ledger_bankdetails',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='ledger_cheque_demension',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='ledger_chequebook',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='ledger_gstvalues',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='ledger_taxreggst',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='rateofexchange',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='tally_group',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='tally_ledger',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='voucher',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
        migrations.AddField(
            model_name='voucher_advanceconf',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
    ]
