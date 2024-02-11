# backend/migrations/0001_initial.py
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=255)),
                ('stock_status', models.CharField(max_length=50)),
                ('available_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('merchant', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('approved', models.BooleanField()),
                ('employee', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='backend.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('extras', models.IntegerField()),
            ],
        ),
    ]
