from django.db import migrations


def migrate_to_product_model(apps, schema_editor):
    Commodity = apps.get_model('commodity', 'Commodity')
    Computer = apps.get_model('computer', 'Computer')

    for computer in Computer.objects.all():
        Commodity.objects.create(
            name=computer.name,
            subcategory=computer.subcategory,
            specification=computer.specification,
            image=computer.image,
            price=computer.price,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_to_product_model)
    ]