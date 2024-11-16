# Generated by Django 5.1.2 on 2024-11-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=45)),
                ('tittle', models.CharField(max_length=60)),
                ('rating', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='team',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=78),
        ),
        migrations.AlterField(
            model_name='team',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=78),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=78),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=78),
        ),
    ]