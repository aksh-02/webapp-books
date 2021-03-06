# Generated by Django 2.1.4 on 2019-01-05 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0006_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(choices=[('Horror', 'Horror'), ('Thriller', 'Thriller'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Biography', 'Biography'), ('Autobiography', 'Autobiography'), ('Sci-Fi', 'Sci-Fi'), ('History', 'History'), ('Children', 'Children'), ('Fiction', 'Fiction'), ('Drama', 'Drama'), ('Poetry', 'Poetry'), ('Mythology', 'Mythology')], max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='genre',
            field=models.ManyToManyField(to='commerce.Genre'),
        ),
    ]
