# Generated by Django 4.1.3 on 2025-01-27 16:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('conteudo', models.TextField(max_length=500)),
                ('autor', models.CharField(max_length=100)),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
