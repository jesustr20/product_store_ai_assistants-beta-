import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")
django.setup()

from categories.models import Category
from products.models import Product

def add_categorys():
    category = ["embutidos", "pescados y mariscos","frescos del día",
                "ensaladas preempacadas","frutas de temporada","botanas",
                "dulces","opciones saludables","detergentes y jabones",
                "productos de limpieza","artículos para el hogar",
                "cuidado personal","artículos para el cuidado femenino",
                "productos para bebés","cervezas","vinos y licores",
                "vinos de menor precio","comidas preparadas",
                "postres congelados","vegetales congelados",
                "medicamentos básicos","primeros auxilios","protección y salud",
                "descuentos"]
    
    for name in category:
        name = name.strip().lower()
        categoria, create = Category.objects.get_or_create(name=name)
        if create:
            print(f"Se agregó: {name}")
        else:
            print(f"Ya existe: {name}")

    products = [        
         {"name": "Choriburger SAN FERNANDO Bolsa 12un", "description": "embutidos san fernando", "price": 16.20, "category":"embutidos"},
         {"name": "Frankfurter Tradicional SALCHICHERÍA ALEMANA Paquete 250g", "description": "embutidos san fernando", "price": 15.10, "category":"embutidos"},
         {"name": "Chorizo Español OTTO KUNZ Paquete 100g", "description": "embutidos san fernando", "price": 19.90, "category":"embutidos"},
         {"name": "Chorizo Finas Hierbas OREGON FOOD'S Paquete 400g", "description": "embutidos san fernando", "price": 17.70, "category":"embutidos"},
         {"name": "Salchicha Frankfurter Clásica BRAEDT Paquete 250g", "description": "embutidos san fernando", "price": 15.70, "category":"embutidos"},
         {"name": "Chorizo Artesanal de Miel de Maple con Tocino LA CHARCUTERÍA Caja 4un", "description": "embutidos san fernando", "price": 27.90, "category":"embutidos"},        
         {"name": "Pack Detergente Líquido ARIEL Pro Cuidado 3L x 2un", "description": "detergentes ace", "price": 93.90, "category": "detergentes y jabones"},
         {"name": "Detergente en Polvo OPAL Ultra Bolsa 2.4kg", "description": "frutas san fernando", "price": 25.59, "category": "detergentes y jabones"},
         {"name": "Pack Detergente en Polvo ARIEL Pro Cuidado 2 kg + Suavizante DOWNY Floral Concentrado 1.4L", "description": "frutas san fernando", "price": 43.19, "category": "detergentes y jabones"},
         {"name": "Jabón BOLIVAR Cuidado Total Bolsa 380g", "description": "jabones", "price": 5.70, "category": "detergentes y jabones", "category": "detergentes y jabones"},
         {"name": "Jabón en Barra PROTEX Avena 3x110g", "description": "frutas san fernando", "price": 10.00, "category": "detergentes y jabones"},
         {"name": "Jabón en Barra PROTEX Fresh 3x110g", "description": "frutas san fernando", "price": 10.90, "category": "detergentes y jabones"},                
         {"name": "Aparato Automático GLADE Edición Limitada + Respuesto Jingle Pear 270ml", "description": "detergentes ace", "price": 48.90, "category": "productos de limpieza"},
         {"name": "Desinfectante de Baño PATO Pastilla Fragancia Marina Empaque 3un", "description": "frutas san fernando", "price": 29.90, "category": "productos de limpieza"},
         {"name": "Detergente en Polvo BOREAL Explosión Floral Bolsa 4kg", "description": "frutas san fernando", "price": 43.19, "category": "productos de limpieza"},
         {"name": "Detergente líquido BOREAL Lavanda Galonera 2L", "description": "jabones", "price": 16.90, "category": "productos de limpieza"},
         {"name": "Detergente Líquido ETERNA Bio Ecológico Botella 2L", "description": "frutas san fernando", "price": 35.90, "category": "productos de limpieza"},
         {"name": "Detergente en Polvo ARIEL con un Toque de Downy para Lavar Ropa Blanca y de Color 4kg", "description": "frutas san fernando", "price": 54.90, "category": "productos de limpieza"},        
    ]

    for product in products:
        category_name = product.pop("category").strip().lower()
        category, _ = Category.objects.get_or_create(name=category_name)

        product_name = product["name"].strip().lower()        
        product, created = Product.objects.get_or_create(name=product_name, defaults={**product, "category":category})

        if created:
            print(f"Producto agregado: {product.name} en la categoria {category.name}")
        else:
            print(f"Producto ya existe: {product.name}")

#add_categorys()
if __name__ == "__main__":
    add_categorys()