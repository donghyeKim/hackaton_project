# Generated by Django 2.1.8 on 2019-07-29 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locally', '0006_auto_20190729_0737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
