# Generated by Django 5.0.6 on 2024-05-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('short_description', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('position', models.CharField(choices=[('administrator', 'Administrator'), ('staff', 'Ishchi'), ('ceo', 'Boshliq')], max_length=13)),
                ('short_description', models.CharField(max_length=255)),
                ('avatar', models.ImageField(upload_to='staff')),
            ],
        ),
    ]