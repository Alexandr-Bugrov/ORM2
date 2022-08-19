# Generated by Django 4.1 on 2022-08-19 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_scope_article_delete_article_scope'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scopes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='scopes', to='articles.article')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.DeleteModel(
            name='Scope',
        ),
        migrations.AddField(
            model_name='scopes',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='scopes', to='articles.tag'),
        ),
    ]