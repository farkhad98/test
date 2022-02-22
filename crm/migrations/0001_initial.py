# Generated by Django 3.2 on 2021-10-14 17:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentPay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='StudentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.group')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('parrent_name', models.CharField(blank=True, max_length=255, null=True)),
                ('parrent_phone', models.CharField(blank=True, max_length=13, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.group')),
                ('pay', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.studentpay')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.studentstatus')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm.subject'),
        ),
    ]
