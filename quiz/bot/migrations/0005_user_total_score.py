# Generated by Django 4.2 on 2023-04-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_alter_user_a1_1_alter_user_a1_2_alter_user_a1_3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
    ]
