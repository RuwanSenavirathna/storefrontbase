# Generated by Django 3.2.7 on 2021-09-03 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zip'),
    ]

    operations = [
        migrations.RunSQL("""
        INSERT INTO store_collection (title)
        VALUES ('collection1')
        """, """
        DELETE FROM store_collection
        WHERE title='collection1'
        """)
    ]