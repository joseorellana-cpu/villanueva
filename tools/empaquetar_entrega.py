import os
import shutil
import json

def empaquetar(cliente_nombre):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    id_cliente = cliente_nombre.lower().replace(" ", "_")
    
    # Buscar en qué carpeta de ventas está el cliente
    ventas_dir = os.path.join(base_dir, 'ventas_realizadas')
    cliente_folder = None
    for folder in os.listdir(ventas_dir):
        if id_cliente in folder.lower():
            cliente_folder = os.path.join(ventas_dir, folder)
            break
    
    if not cliente_folder or not os.path.exists(cliente_folder):
        print(f"ERROR: No se encontro carpeta para '{cliente_nombre}' en ventas_realizadas/")
        print("Genera la invitacion primero con el script correspondiente.")
        return
    
    # Crear carpeta de entregables
    entregables_dir = os.path.join(base_dir, 'entregables')
    os.makedirs(entregables_dir, exist_ok=True)
    
    zip_path = os.path.join(entregables_dir, f'Invitacion_{cliente_nombre.replace(" ", "_")}')
    shutil.make_archive(zip_path, 'zip', cliente_folder)
    
    print("=" * 50)
    print(f"PAQUETE LISTO PARA ENVIAR")
    print(f"Cliente: {cliente_nombre}")
    print(f"Archivo: {zip_path}.zip")
    print("=" * 50)
    print("\nInstrucciones para enviar al cliente:")
    print("1. Envia el archivo .zip por WhatsApp")
    print("2. El cliente debe descomprimirlo")
    print("3. Abrir el archivo index.html en su navegador")
    print("4. Compartir el link o el archivo con sus invitados")

if __name__ == "__main__":
    nombre = input("Nombre del cliente: ")
    empaquetar(nombre)