# Generated by Django 4.0 on 2022-01-03 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='offer',
            name='Client',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='Hairdresser',
        ),
        migrations.AddField(
            model_name='offer',
            name='Name',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='Price',
            field=models.IntegerField(default='0'),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client', models.TextField()),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Barber', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.barber')),
                ('Offer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.offer')),
            ],
        ),
        migrations.AddField(
            model_name='Reservation',
            name='Time',
            field=models.DateField(),
        ),
    ]
