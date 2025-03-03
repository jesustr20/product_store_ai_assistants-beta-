import os
import shutil
import django
from django.conf import settings

"""Borra los archivos temporales y los acrhivos de migraciones
Para correr nuevamente la db y generar todo de nuevo, solo es temporal"""

def delete_pycache(root_directory):
    for root, dirs, files in os.walk(root_directory):
        for dir_name in dirs:
            if dir_name=="__pycache__":
                pycache_path = os.path.join(root, dir_name)
                print(f"Borrado carpeta: {pycache_path}")
                shutil.rmtree(pycache_path)

def delete_migrations(root_directory):
    for root, dirs, files in os.walk(root_directory):
        if 'migrations' in dirs:
            migration_path = os.path.join(root, 'migrations')
            for file_name in os.listdir(migration_path):
                if file_name != '__init__.py' and file_name.endswith('.py'):
                    file_path = os.path.join(migration_path, file_name)
                    print(f"Borrado archivo de migración: {file_path}")
                    os.remove(file_path)

def delete_database_sqlite3():
    database_settings = settings.DATABASES['default']
    db_engine = database_settings['ENGINE']

    if 'sqlite3' in db_engine:
        db_path = database_settings['NAME']
        if os.path.exists(db_path):
            print(f"Borrado archivo de base de datos SQLite: {db_path}")
            os.remove(db_path)
        else:
            print(f"No se encontró la base de datos SQLite: {db_path}")
    else:
        db_name = database_settings('NAME')
        print(f"La base de datos '{db_name}' no es SQLite. Elimina manualmente la base de datos en el servidor.")
        print(f"Base de datos detectada: {db_engine}")

def get_django_settings_module():
    """
    Recorre los directorios padres a partir de este archivo hasta encontrar 'manage.py'.
    Asume que el nombre del directorio que contiene 'manage.py' es el nombre del proyecto,
    y que el módulo de settings es '<project_name>.settings'.
    """
    current_dir = os.path.abspath(os.path.dirname(__file__))
    for root, dirs, files in os.walk(current_dir):
        if "settings.py" in files:
            # Suponemos que el directorio que contiene settings.py es el que queremos usar
            settings_dir = os.path.basename(root)
            return f"{settings_dir}.settings"
    raise RuntimeError("No se encontró 'settings.py' en ningún directorio.")

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', get_django_settings_module())

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', get_django_settings_module())
    django.setup()

    project_root = os.path.dirname(os.path.abspath(__file__))

    delete_pycache(project_root)
    delete_migrations(project_root)
    delete_database_sqlite3()

    print("Limpieza completada.")