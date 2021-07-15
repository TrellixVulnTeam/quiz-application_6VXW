# Generated by Django 3.2.4 on 2021-06-09 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scored', models.IntegerField(default=0)),
                ('totalScored', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.test')),
            ],
        ),
    ]
