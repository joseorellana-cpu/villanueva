import json
import os

def build_premium():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'cliente_premium.json')
    
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    template_path = os.path.join(base_dir, 'plantillas', 'cumpleaños', 'invitacion-premium.html')
    
    with open(template_path, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # 1. Inyectar CONFIG en el JS
    config_str = f"const CONFIG = {{ nombre: '{data['nombre']}', telefono: '{data['telefono_whatsapp']}' }};"
    html = html.replace("const CONFIG = { nombre: 'Rocío' };", config_str)
    
    # 2. Inyectar fecha del evento para el countdown
    fecha_evento = data.get('fecha_evento', '2026-12-15T20:00:00')
    html = html.replace("new Date('2026-12-15T20:00:00')", f"new Date('{fecha_evento}')")
    
    # 3. Inyectar número de WhatsApp en el botón de confirmación
    html = html.replace('https://wa.me/?text=', f"https://wa.me/{data['telefono_whatsapp']}?text=")
    
    # 4. Reemplazar el mensaje de la carta si se proporciona uno personalizado
    if 'mensaje_personalizado' in data:
        old_mensagem = "Quise regalarte algo distinto: un pequeño jardín hecho con cariño, donde cada flor y cada fresa lleva un deseo para ti."
        html = html.replace(old_mensagem, data['mensaje_personalizado'])
        
    # 5. Guardar el resultado
    out_dir = os.path.join(base_dir, 'ventas_realizadas', 'cliente_premium_001')
    os.makedirs(out_dir, exist_ok=True)
    
    out_path = os.path.join(out_dir, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(">>> Invitacion PREMIUM generada exitosamente en:", out_path)

if __name__ == "__main__":
    build_premium()