from django.db import migrations

def migrate_to_product_model(apps, schema_editor):
    Product = apps.get_model('product', 'Product')
    Shoes = apps.get_model('shoe', 'Shoes')
    Computer = apps.get_model('computer', 'Computer')

    for shoe in Shoes.objects.all():
        Product.objects.create(
            name=shoe.name,
            brand=shoe.brand,
            color=shoe.color,
            in_stock=shoe.in_stock,
            description=shoe.description,
            image=shoe.image,
            product_type="shoe"
        )

    for computer in Computer.objects.all():
        Product.objects.create(
            name=computer.name,
            brand=computer.brand,
            color=computer.color,
            in_stock=computer.in_stock,
            description=computer.description,
            image=computer.image,
            product_type="computer"
        )


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_to_product_model)
    ]