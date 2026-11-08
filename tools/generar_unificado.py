import json
import os
import shutil

TEMPLATES = {
    "1": {
        "nombre": "Cumpleaños Premium",
        "template": "plantillas/cumpleaños/invitacion-premium.html",
        "data_file": "data/cliente_premium.json",
        "config_marker": "const CONFIG = { nombre: 'Rocío' };",
        "build_script": "tools/build_premium.py",
        "precio": "$12 USD"
    },
    "2": {
        "nombre": "Boda Elegante",
        "template": "plantillas/bodas/invitacion-boda-elegante.html",
        "data_file": "data/cliente_boda.json",
        "config_marker": "const CONFIG = { nombre: 'María & Juan', telefono: '' };",
        "build_script": "tools/build_boda.py",
        "precio": "$20 USD"
    },
    "3": {
        "nombre": "Quinceañera Elegante",
        "template": "plantillas/quinceañera/invitacion-xv-elegante.html",
        "data_file": "data/cliente_quince.json",
        "config_marker": "const CONFIG = { nombre: 'Valentina', telefono: '' };",
        "build_script": "tools/build_quince.py",
        "precio": "$18 USD"
    }
}

def main():
    print("=" * 60)
    print("   GENERADOR UNIFICADO DE INVITACIONES - VILLA NUEVA")
    print("=" * 60)
    print("\nPlantillas disponibles:")
    for key, info in TEMPLATES.items():
        print(f"  {key}. {info['nombre']} ({info['precio']})")
    
    opcion = input("\nSelecciona plantilla (1/2/3): ").strip()
    if opcion not in TEMPLATES:
        print("Opcion invalida.")
        return
    
    info = TEMPLATES[opcion]
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print(f"\n--- Generando: {info['nombre']} ---")
    nombre = input("Nombre del homenajeado/a: ").strip()
    telefono = input("Telefono WhatsApp (sin +): ").strip()
    fecha = input("Fecha del evento (YYYY-MM-DDTHH:MM:SS): ").strip()
    mensaje = input("Mensaje personalizado (Enter para default): ").strip()
    
    # Leer template
    template_path = os.path.join(base_dir, info['template'])
    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Inyectar CONFIG
    config_str = f"const CONFIG = {{ nombre: '{nombre}', telefono: '{telefono}' }};"
    html = html.replace(info['config_marker'], config_str)
    
    # Inyectar fecha
    fecha_default = "2026-12-15T20:00:00"
    html = html.replace(f"new Date('{fecha_default}')", f"new Date('{fecha}')")
    
    # Inyectar WhatsApp
    html = html.replace('https://wa.me/" + CONFIG.telefono + "?text=', f"https://wa.me/{telefono}?text=")
    html = html.replace('https://wa.me/?text=', f"https://wa.me/{telefono}?text=")
    
    # Reemplazar mensaje si se proporciona
    if mensaje:
        # Buscar y reemplazar el primer parrafo del sheet
        import re
        html = re.sub(r'(<div class="sheet">.*?<p>)(.*?)(</p>)', rf'\1{mensaje}\3', html, count=1, flags=re.DOTALL)
    
    # Guardar
    id_cliente = nombre.lower().replace(" ", "_").replace("&", "y")
    out_dir = os.path.join(base_dir, 'ventas_realizadas', f'cliente_{id_cliente}')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    # Empaquetar
    entregables_dir = os.path.join(base_dir, 'entregables')
    os.makedirs(entregables_dir, exist_ok=True)
    zip_path = os.path.join(entregables_dir, f'Invitacion_{nombre.replace(" ", "_")}')
    shutil.make_archive(zip_path, 'zip', out_dir)
    
    print("\n" + "=" * 60)
    print(f"INVITACION GENERADA: {info['nombre']}")
    print(f"HTML: {out_path}")
    print(f"ZIP: {zip_path}.zip")
    print("=" * 60)
    print("\nInstrucciones de entrega:")
    print("1. Envia el archivo .zip al cliente por WhatsApp")
    print("2. El cliente descomprime y abre index.html")
    print("3. El cliente comparte el link con sus invitados")

if __name__ == "__main__":
    main()