# Generated by Django 2.0.1 on 2019-05-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='guangMoKuai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changjia', models.CharField(max_length=50)),
                ('xinghao', models.CharField(max_length=100)),
                ('chengZaiWang', models.IntegerField()),
                ('chengYuWang', models.IntegerField()),
                ('moveTo750', models.IntegerField()),
            ],
        ),
    ]
