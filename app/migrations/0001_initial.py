# Generated by Django 2.2.7 on 2019-11-06 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuizSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='testing@testing.com', max_length=254)),
                ('photo', models.ImageField(upload_to='user_img')),
            ],
        ),
    ]
