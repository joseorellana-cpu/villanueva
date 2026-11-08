# 🎉 Villa Nueva - Invitaciones Digitales Interactivas

## 💰 Modelo de Negocio
Vende invitaciones digitales interactivas con animaciones, música y confirmación por WhatsApp.

### Precios Sugeridos
| Producto | Precio | Nicho |
|----------|--------|-------|
| Cumpleaños Premium | $12 USD | Cumpleaños, fiestas |
| Boda Elegante | $20 USD | Bodas, eventos formales |
| Evento Corporativo | $25 USD | Empresas, celebraciones |

---

## 📁 Estructura del Proyecto
```
Villa Nueva/
├── index.html                    # Catálogo de ventas (GitHub Pages)
├── plantillas/
│   ├── cumpleaños/
│   │   └── invitacion-premium.html   # Plantilla cumpleaños
│   └── bodas/
│       └── invitacion-boda-elegante.html  # Plantilla bodas
├── tools/
│   ├── build_premium.py          # Genera invitación cumpleaños
│   ├── build_boda.py             # Genera invitación boda
│   └── empaquetar_entrega.py     # Empaqueta para envío
├── data/
│   ├── cliente_premium.json      # Datos ejemplo cumpleaños
│   └── cliente_boda.json         # Datos ejemplo boda
├── ventas_realizadas/            # Invitaciones generadas
├── entregables/                  # ZIPs listos para enviar
└── docs/
    ├── PLAN_ESTRATEGICO.md
    └── GUIA_PRIMERA_VENTA.md
```

---

## 🚀 Flujo de Venta (5 minutos por cliente)

### Paso 1: Recibir pedido del cliente
Pide al cliente: Nombre, Fecha, Hora, Lugar, Teléfono WhatsApp, Mensaje personalizado

### Paso 2: Generar invitación
```bash
# Para cumpleaños:
python tools/build_premium.py

# Para bodas:
python tools/build_boda.py
```
Edita el archivo `data/cliente_premium.json` o `data/cliente_boda.json` con los datos del cliente antes de ejecutar.

### Paso 3: Empaquetar para entrega
```bash
python tools/empaquetar_entrega.py
```
Ingresa el nombre del cliente cuando se solicite.

### Paso 4: Enviar al cliente
Envía el archivo `.zip` de la carpeta `entregables/` por WhatsApp.

---

## 📱 Catálogo en Vivo
Tu catálogo está disponible en:
**https://joseorellana-cpu.github.io/lab08_empre/**

---

## 💡 Tips de Venta
1. Graba un video de 15s mostrando la animación del sobre
2. Publica en TikTok/Instagram Reels con audio en tendencia
3. Comparte en grupos de Facebook de tu ciudad
4. Ofrece "primera unidad gratis a cambio de testimonio" para empezar

---

## ⚡ Automatización Total
- **Tiempo por cliente:** 5 minutos
- **Margen de utilidad:** ~95%
- **Costo de producción:** $0 (producto digital)
- **Entrega:** Inmediata por WhatsApp

---

## 📞 Contacto
WhatsApp: [Tu número aquí]
Email: [Tu email aquí]