# Generated by Django 3.2 on 2024-10-29 00:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_form_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_name', models.CharField(max_length=64)),
                ('message', models.TextField()),
            ],
        ),
    ]