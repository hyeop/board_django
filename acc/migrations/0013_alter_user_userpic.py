# Generated by Django 3.2.7 on 2021-09-28 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0012_alter_user_userpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userpic',
            field=models.ImageField(upload_to='usr/%y'),
        ),
    ]
