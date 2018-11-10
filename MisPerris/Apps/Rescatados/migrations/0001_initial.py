# Generated by Django 2.1.2 on 2018-10-13 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tamanio', models.CharField(max_length=10)),
                ('peso', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=80)),
                ('fechaRescate', models.DateField()),
                ('Estado', models.CharField(choices=[('R', 'Rescatado'), ('D', 'Disponible'),('A','Adoptado')], default='M', max_length=1)),
            ],
        )
    ]