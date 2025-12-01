import flet as ft
import json
import os
import webbrowser
from datetime import datetime
import math
def main(page: ft.Page):
    # Configuración de la página
    page.title = "🚨 App Sismos CDMX"
    page.bgcolor = "#FFFFFF"
    page.padding = 0
    page.window_width = 400
    page.window_height = 800
    page.window_min_width = 300
    page.window_min_height = 600
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Datos globales
    contactos = []
    kit_emergencia = []
    
    # ========== CREADORAS ==========
    CREADORAS = [
        "Vazquez Torralva Abigail Valeria",
        "Cabrera Cruz Yareli Rubi", 
        "Ramirez Bautista Jimena Montserrat",
        "Ortiz Garcia Italia Nicole"
    ]
    
    # ========== FUNCIONES AUXILIARES ==========
    def mostrar_snack_bar(mensaje, color="#4CAF50"):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensaje),
            bgcolor=color
        )
        page.snack_bar.open = True
        page.update()
    
    def llamar_cruz_roja(e):
        mostrar_snack_bar("📞 Llamando a Cruz Roja...", "#D32F2F")
    
    def llamar_proteccion_civil(e):
        mostrar_snack_bar("📞 Llamando a Protección Civil...", "#D32F2F")
    
    # ========== FUNCIÓN PARA VOLVER AL MENÚ ==========
    def volver_menu(e):
        page.clean()
        mostrar_menu()
    
    # ========== MENÚ PRINCIPAL ==========
    def mostrar_menu():
        page.clean()
        
        # Encabezado
        encabezado = ft.Container(
            content=ft.Column([
                ft.Text("🚨", size=40, text_align=ft.TextAlign.CENTER),
                ft.Text(
                    "APP SISMOS CDMX",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color="#FFFFFF"
                ),
                ft.Text(
                    "Sistema de Prevención Sísmica",
                    size=14,
                    text_align=ft.TextAlign.CENTER,
                    color="#FFCDD2"
                ),
                ft.Text(
                    "Creado por:",
                    size=10,
                    text_align=ft.TextAlign.CENTER,
                    color="#FFCDD2",
                    opacity=0.8
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            bgcolor="#C62828",
            padding=20,
            height=170
        )
        
        # Lista de creadoras
        creadoras_text = ft.Text(
            "👩‍💻 " + " | ".join(CREADORAS),
            size=12,
            color="#FFFFFF",
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.W_500
        )
        
        encabezado.content.controls.append(creadoras_text)
        
        # Función para crear botones
        def crear_boton(texto, color, accion, icono=""):
            return ft.Container(
                content=ft.ElevatedButton(
                    text=f"{icono} {texto}" if icono else texto,
                    bgcolor=color,
                    color="#FFFFFF",
                    width=350,
                    height=60,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                    on_click=accion
                ),
                margin=5
            )
        
        # Lista de botones
        botones = ft.Column([
            crear_boton(
                "Información de Sismos",
                "#E53935",
                lambda e: pantalla_info_sismos(),
                "📊"
            ),
            crear_boton(
                "Recomendaciones Preventivas",
                "#E53935",
                lambda e: pantalla_prevencion(),
                "🛡️"
            ),
            crear_boton(
                "Instrucciones DURANTE Sismo",
                "#E53935",
                lambda e: pantalla_durante_sismo(),
                "⚠️"
            ),
            crear_boton(
                "Acciones DESPUÉS del Sismo",
                "#E53935",
                lambda e: pantalla_post_sismo(),
                "✅"
            ),
            crear_boton(
                "BOTÓN SOS",
                "#B71C1C",
                lambda e: pantalla_sos(),
                "🆘"
            ),
            crear_boton(
                "Registrar Sismo",
                "#F57C00",
                lambda e: pantalla_registrar(),
                "📝"
            ),
            crear_boton(
                "Kit de Emergencia",
                "#F57C00",
                lambda e: pantalla_kit(),
                "🎒"
            ),
            crear_boton(
                "Contactos de Emergencia",
                "#F57C00",
                lambda e: pantalla_contactos(),
                "📞"
            ),
        ], scroll=ft.ScrollMode.AUTO, spacing=0)
        
        # Agregar todo a la página
        page.add(
            encabezado,
            ft.Container(
                content=botones,
                alignment=ft.alignment.center,
                padding=15,
                expand=True
            )
        )
        page.update()
    
    # ========== PANTALLA INFO SISMOS ==========
    def pantalla_info_sismos():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "📊 SISMOS RECIENTES",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        # Datos de sismos más realistas
        sismos = [
            {"fecha": "15 Enero 2024", "magnitud": 5.2, "epicentro": "Guerrero", "prof": 45, "intensidad": "VI"},
            {"fecha": "10 Enero 2024", "magnitud": 4.8, "epicentro": "Oaxaca", "prof": 12, "intensidad": "V"},
            {"fecha": "05 Enero 2024", "magnitud": 3.9, "epicentro": "Puebla", "prof": 58, "intensidad": "IV"},
            {"fecha": "28 Diciembre 2023", "magnitud": 6.1, "epicentro": "Michoacán", "prof": 20, "intensidad": "VII"},
            {"fecha": "20 Diciembre 2023", "magnitud": 4.5, "epicentro": "Estado de México", "prof": 35, "intensidad": "V"}
        ]
        
        # Crear tarjetas
        def crear_tarjeta_sismo(sismo):
            # Color según magnitud
            if sismo['magnitud'] < 4.0:
                color_magnitud = "#4CAF50"
                nivel = "Menor"
            elif sismo['magnitud'] < 5.0:
                color_magnitud = "#FFC107"
                nivel = "Ligero"
            elif sismo['magnitud'] < 6.0:
                color_magnitud = "#FF9800"
                nivel = "Moderado"
            else:
                color_magnitud = "#F44336"
                nivel = "Fuerte"
            
            return ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text(f"📅 {sismo['fecha']}", weight=ft.FontWeight.BOLD, size=14),
                            ft.Container(
                                content=ft.Text(f"{sismo['magnitud']}", color="white", weight=ft.FontWeight.BOLD),
                                bgcolor=color_magnitud,
                                padding=5,
                                border_radius=5
                            )
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text(f"Epicentro: {sismo['epicentro']}", size=12),
                        ft.Text(f"Profundidad: {sismo['prof']} km", size=12),
                        ft.Text(f"Intensidad: {sismo['intensidad']} - {nivel}", size=12, color=color_magnitud, weight=ft.FontWeight.BOLD),
                    ]),
                    padding=15,
                    width=350
                ),
                elevation=3,
                color="#FFFFFF"
            )
        
        lista_sismos = ft.Column([
            crear_tarjeta_sismo(sismo) for sismo in sismos
        ], spacing=10, scroll=ft.ScrollMode.AUTO)
        
        page.add(
            encabezado,
            ft.Container(content=lista_sismos, padding=15, expand=True),
            ft.Container(
                content=ft.Text(
                    "📡 Fuente: Servicio Sismológico Nacional",
                    size=12,
                    color="#616161",
                    text_align=ft.TextAlign.CENTER
                ),
                padding=10
            )
        )
        page.update()
    
    # ========== PANTALLA PREVENCIÓN ==========
    def pantalla_prevencion():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "🛡️ PREVENCIÓN",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        recomendaciones = [
            "Identifica las ZONAS SEGURAS en tu casa, escuela y trabajo",
            "Participa en SIMULACROS regularmente",
            "Prepara un KIT DE EMERGENCIA familiar completo",
            "Asegura MUEBLES PESADOS a las paredes",
            "Conoce la ubicación de LLAVES de gas, agua y electricidad",
            "Ten a la mano CONTACTOS DE EMERGENCIA actualizados",
            "Revisa que tu edificio cumpla con NORMAS ANTISÍSMICAS",
            "Mantén DOCUMENTOS IMPORTANTES en lugar accesible",
            "Establece un PUNTO DE REUNIÓN familiar",
            "Descarga la app de ALERTA SÍSMICA oficial del SASMEX",
            "Mantén siempre la BATERÍA del celular cargada",
            "Ten siempre una LINTERNA en lugar accesible"
        ]
        
        def crear_card_recomendacion(texto):
            return ft.Card(
                content=ft.Container(
                    content=ft.Row([
                        ft.Text("✅", size=24),
                        ft.Text(texto, size=13, expand=True)
                    ]),
                    padding=12,
                    width=350
                ),
                elevation=2,
                color="#E8F5E9"
            )
        
        lista_recomendaciones = ft.Column([
            crear_card_recomendacion(rec) for rec in recomendaciones
        ], spacing=8, scroll=ft.ScrollMode.AUTO)
        
        page.add(
            encabezado,
            ft.Container(content=lista_recomendaciones, padding=15, expand=True),
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "⚠️ La preparación salva vidas",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#C62828",
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "🏃‍♂️ La respuesta en los primeros 3 minutos es crucial",
                        size=12,
                        color="#666666",
                        text_align=ft.TextAlign.CENTER
                    )
                ]),
                padding=15
            )
        )
        page.update()
    
    # ========== PANTALLA DURANTE SISMO ==========
    def pantalla_durante_sismo():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "⚠️ DURANTE EL SISMO",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        # Texto de instrucciones
        texto_instrucciones = ft.Text(
            "Selecciona tu ubicación para ver instrucciones específicas",
            size=14,
            color="#000000",
            text_align=ft.TextAlign.CENTER
        )
        
        area_instrucciones = ft.Container(
            content=texto_instrucciones,
            bgcolor="#FFEBEE",
            padding=20,
            border_radius=10,
            expand=True
        )
        
        # Función para mostrar instrucciones
        def mostrar_instrucciones(ubicacion):
            instrucciones = {
                "casa": """🏠 EN CASA:
🔺 MANTÉN LA CALMA
🔺 AGÁCHATE, CÚBLETE Y SÚJETATE
🔺 Aléjate de VENTANAS y ESPEJOS
🔺 Protégete bajo MESA RESISTENTE
🔺 Aléjate de objetos que puedan caer
🔺 NO uses ELEVADORES
🔺 NO salgas durante el temblor
🔺 Mantente alejado de estufas
⚠️ REGLA DE ORO: AGÁCHATE, CÚBLETE, SÚJETATE""",
                
                "escuela": """🏫 EN ESCUELA:
🔺 Sigue indicaciones del MAESTRO inmediatamente
🔺 Ubícate en ZONA SEGURA del salón
🔺 AGÁCHATE, CÚBRETSE y SÚJETATE bajo tu pupitre
🔺 Aléjate de VENTANAS y objetos colgantes
🔺 Protege CABEZA y CUELLO con tus brazos
🔺 NO corras hacia salidas durante el sismo
🔺 Mantén la calma y escucha instrucciones
⚠️ ZONA SEGURA ESCOLAR""",
                
                "oficina": """🏢 EN OFICINA:
🔺 AGÁCHATE bajo tu ESCRITORIO
🔺 Aléjate de VENTANALES inmediatamente
🔺 SÚJETATE del escritorio firmemente
🔺 NO uses ELEVADORES
🔺 Aléjate de LIBREROS y archiveros
🔺 Si estás en piso alto, NO bajes corriendo
🔺 Espera a que termine el movimiento
⚠️ PROTÉGETE BAJO TU ESCRITORIO""",
                
                "vehiculo": """🚗 EN VEHÍCULO:
🔺 DETENTE en lugar seguro (no en puentes)
🔺 Apaga el motor pero mantén las luces encendidas
🔺 Aléjate de PUENTES, túneles y cables eléctricos
🔺 Permanece DENTRO del vehículo
🔺 Enciende luces INTERMITENTES
🔺 Escucha la RADIO para información
🔺 Mantén las ventanillas ligeramente abiertas
⚠️ NO SALGAS DEL AUTO""",
                
                "calle": """🛣️ EN LA CALLE:
🔺 AGÁCHATE en ESPACIO ABIERTO
🔺 Aléjate de EDIFICIOS, POSTES y anuncios
🔺 Busca ÁREA SEGURA sin construcciones
🔺 Protege tu CABEZA con los brazos
🔺 Aléjate de CABLES eléctricos caídos
🔺 NO te acerques a fachadas dañadas
🔺 Busca PARQUES o áreas despejadas
⚠️ BUSCA ESPACIO ABIERTO Y AGÁCHATE"""
            }
            texto_instrucciones.value = instrucciones.get(ubicacion, "Selecciona una ubicación para ver instrucciones")
            page.update()
        
        # Botones de ubicación
        botones = ft.Column([
            ft.Text("¿Dónde te encuentras?", size=16, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
            ft.Row([
                ft.ElevatedButton(
                    "🏠 Casa",
                    bgcolor="#1976D2",
                    color="#FFFFFF",
                    expand=True,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                    on_click=lambda e: mostrar_instrucciones("casa")
                ),
                ft.ElevatedButton(
                    "🏫 Escuela",
                    bgcolor="#1976D2",
                    color="#FFFFFF",
                    expand=True,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                    on_click=lambda e: mostrar_instrucciones("escuela")
                )
            ], spacing=10),
            ft.Row([
                ft.ElevatedButton(
                    "🏢 Oficina",
                    bgcolor="#1976D2",
                    color="#FFFFFF",
                    expand=True,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                    on_click=lambda e: mostrar_instrucciones("oficina")
                ),
                ft.ElevatedButton(
                    "🚗 Vehículo",
                    bgcolor="#1976D2",
                    color="#FFFFFF",
                    expand=True,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                    on_click=lambda e: mostrar_instrucciones("vehiculo")
                )
            ], spacing=10),
            ft.ElevatedButton(
                "🛣️ Calle",
                bgcolor="#1976D2",
                color="#FFFFFF",
                width=350,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                on_click=lambda e: mostrar_instrucciones("calle")
            )
        ], spacing=10)
        
        page.add(
            encabezado,
            ft.Container(content=botones, padding=15),
            ft.Container(content=area_instrucciones, padding=15, expand=True)
        )
        page.update()
    
    # ========== PANTALLA POST SISMO ==========
    def pantalla_post_sismo():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "✅ DESPUÉS DEL SISMO",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        acciones = [
            "1️⃣ MANTÉN LA CALMA y verifica tu estado físico",
            "2️⃣ Revisa si hay LESIONADOS y presta primeros auxilios",
            "3️⃣ EVACÚA si es necesario, sin correr hacia salidas",
            "4️⃣ Verifica FUGAS DE GAS (por olor, NO uses fuego)",
            "5️⃣ Cierra las llaves de GAS, AGUA y electricidad",
            "6️⃣ Desconecta la ELECTRICIDAD si hay daños visibles",
            "7️⃣ NO enciendas cerillos, fósforos ni use interruptores",
            "8️⃣ Revisa DAÑOS ESTRUCTURALES en el edificio",
            "9️⃣ Usa el teléfono SOLO para emergencias urgentes",
            "🔟 Mantente informado por RADIO o TV oficial",
            "1️⃣1️⃣ Busca RÉPLICAS - pueden venir después",
            "1️⃣2️⃣ Verifica si tu familia está segura",
            "1️⃣3️⃣ Ten cuidado con CRISTALES ROTOS",
            "1️⃣4️⃣ Si estás en un lugar seguro, permanece ahí"
        ]
        
        lista = ft.Column([
            ft.Card(
                content=ft.Container(
                    content=ft.Text(accion, size=14),
                    padding=15,
                    width=350
                ),
                elevation=2,
                color="#E8F5E9"
            ) for accion in acciones
        ], spacing=8, scroll=ft.ScrollMode.AUTO)
        
        page.add(
            encabezado,
            ft.Container(content=lista, padding=15, expand=True),
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "⏰ Las réplicas pueden ocurrir minutos, horas o días después",
                        size=14,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        color="#E65100"
                    ),
                    ft.Text(
                        "🎯 El sismo principal puede tener réplicas durante semanas",
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                        color="#666666"
                    )
                ]),
                padding=15,
                bgcolor="#FFF3E0"
            )
        )
        page.update()
    
    # ========== PANTALLA SOS ==========
    def pantalla_sos():
        page.clean()
        page.bgcolor = "#B71C1C"
        
        def confirmar_llamada_911(e):
            def cerrar_dialogo(e):
                dialogo.open = False
                page.update()
            
            def confirmar_llamada(e):
                dialogo.open = False
                page.update()
                mostrar_snack_bar("📞 Simulando llamada al 911...")
            
            dialogo = ft.AlertDialog(
                title=ft.Text("⚠️ LLAMADA DE EMERGENCIA", color="#B71C1C", weight=ft.FontWeight.BOLD),
                content=ft.Text("¿Confirmas llamar al 911?"),
                actions=[
                    ft.TextButton("SÍ, LLAMAR", on_click=confirmar_llamada),
                    ft.TextButton("Cancelar", on_click=cerrar_dialogo)
                ]
            )
            page.dialog = dialogo
            dialogo.open = True
            page.update()
        
        # FUNCIÓN MEJORADA PARA GEOLOCALIZACIÓN
        def obtener_ubicacion_mejorada(e):
            def mostrar_ubicacion_dialog(lat, lon, precision, direccion=""):
                def cerrar_dialogo(e):
                    dialogo.open = False
                    page.update()
                
                def copiar_coordenadas(e):
                    coordenadas = f"Lat: {lat:.6f}, Lon: {lon:.6f}"
                    page.set_clipboard(coordenadas)
                    mostrar_snack_bar("📋 Coordenadas copiadas al portapapeles", "#2196F3")
                
                def abrir_mapa(e):
                    maps_url = f"https://maps.google.com/?q={lat},{lon}"
                    webbrowser.open(maps_url)
                    mostrar_snack_bar("🌐 Abriendo mapa en navegador", "#2196F3")
                
                # Generar texto de ubicación en lenguaje natural
                def determinar_ubicacion(lat, lon):
                    ubicaciones_cercanas = {
                        (19.4326, -99.1332): "Centro de Ciudad de México",
                        (19.3979, -99.1647): "Coyoacán, CDMX",
                        (19.3650, -99.1686): "Tlalpan, CDMX",
                        (19.4156, -99.1795): "Benito Juárez, CDMX",
                        (19.3458, -99.1879): "Miguel Hidalgo, CDMX",
                        (19.3998, -99.1966): "Cuauhtémoc, CDMX",
                        (19.3847, -99.1612): "Álvaro Obregón, CDMX",
                        (19.4203, -99.2013): "Gustavo A. Madero, CDMX",
                        (19.3465, -99.1399): "Venustiano Carranza, CDMX"
                    }
                    
                    for (lat_ref, lon_ref), nombre in ubicaciones_cercanas.items():
                        distancia = math.sqrt((lat - lat_ref)**2 + (lon - lon_ref)**2) * 111  # km aprox
                        if distancia < 5:  # Dentro de 5 km
                            return nombre
                    
                    return f"Coordenadas {abs(lat):.4f}°{'N' if lat >= 0 else 'S'}, {abs(lon):.4f}°{'W' if lon >= 0 else 'E'}"
                
                ubicacion_texto = determinar_ubicacion(lat, lon)
                
                dialogo = ft.AlertDialog(
                    title=ft.Text("📍 MI UBICACIÓN ACTUAL", color="#1976D2", weight=ft.FontWeight.BOLD),
                    content=ft.Column([
                        ft.Text(f"📍 Ubicación: {ubicacion_texto}", weight=ft.FontWeight.BOLD),
                        ft.Text(f"🌐 Coordenadas:", weight=ft.FontWeight.BOLD),
                        ft.Text(f"Latitud: {lat:.6f}"),
                        ft.Text(f"Longitud: {lon:.6f}"),
                        ft.Text(f"📊 Precisión: ±{precision:.0f} metros"),
                        ft.Divider(),
                        ft.Text("🔧 Opciones:", weight=ft.FontWeight.BOLD),
                        ft.Text("• Ubicación obtenida correctamente", color="#4CAF50"),
                        ft.Text("• Puedes copiar coordenadas o abrir mapa", size=12, color="#666666")
                    ], tight=True),
                    actions=[
                        ft.TextButton("📋 Copiar", on_click=copiar_coordenadas),
                        ft.TextButton("🗺️ Mapa", on_click=abrir_mapa),
                        ft.TextButton("Cerrar", on_click=cerrar_dialogo)
                    ]
                )
                page.dialog = dialogo
                dialogo.open = True
                page.update()
            
            # Simulación mejorada de geolocalización
            def obtener_coordenadas_simulation():
                # Coordenadas base de CDMX
                base_lat = 19.4326
                base_lon = -99.1332
                
                # Agregar variación aleatoria pequeña
                import random
                lat_offset = random.uniform(-0.01, 0.01)  # ±~1km
                lon_offset = random.uniform(-0.01, 0.01)
                
                lat = base_lat + lat_offset
                lon = base_lon + lon_offset
                precision = random.uniform(5, 50)  # 5-50 metros de precisión
                
                return lat, lon, precision
            
            lat_demo, lon_demo, precision_demo = obtener_coordenadas_simulation()
            mostrar_ubicacion_dialog(lat_demo, lon_demo, precision_demo)
        
        # NUEVA FUNCIÓN: ENVIAR UBICACIÓN POR WHATSAPP
        def enviar_ubicacion_whatsapp(e):
            def enviar_whatsapp_con_contacto(e):
                # Obtener coordenadas simuladas para WhatsApp
                import random
                lat = 19.4326 + random.uniform(-0.01, 0.01)
                lon = -99.1332 + random.uniform(-0.01, 0.01)
                
                # Formatear mensaje para WhatsApp
                mensaje = f"🚨 EMERGENCIA - SISMO DETECTADO\n\n"
                mensaje += f"📍 Mi ubicación es:\n"
                mensaje += f"Latitud: {lat:.6f}\n"
                mensaje += f"Longitud: {lon:.6f}\n\n"
                mensaje += f"🗺️ Ver en Google Maps:\n"
                mensaje += f"https://maps.google.com/?q={lat},{lon}\n\n"
                mensaje += f"⏰ Enviado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                mensaje += f"📱 App Sismos CDMX"
                
                # URL para WhatsApp Web
                mensaje_codificado = mensaje.replace(' ', '%20').replace('\n', '%0A')
                whatsapp_url = f"https://wa.me/?text={mensaje_codificado}"
                
                # Abrir WhatsApp Web
                webbrowser.open(whatsapp_url)
                
                mostrar_snack_bar("📱 Abriendo WhatsApp para enviar ubicación...")
                
                dialogo.open = False
                page.update()
            
            def enviar_ubicacion_sms(e):
                enviar_whatsapp_con_contacto(e)
            
            dialogo = ft.AlertDialog(
                title=ft.Text("📱 ENVÍO DE UBICACIÓN", color="#25D366", weight=ft.FontWeight.BOLD),
                content=ft.Column([
                    ft.Text("¿Cómo quieres enviar tu ubicación?", weight=ft.FontWeight.BOLD),
                    ft.Text("• WhatsApp: Envía mensaje directo a contactos", size=12, color="#666666"),
                    ft.Text("• SMS: Envía por mensaje de texto", size=12, color="#666666"),
                    ft.Divider(),
                    ft.Text("📋 Mensaje que se enviará:", size=12, color="#666666"),
                    ft.Text("• Ubicación GPS actual", size=10),
                    ft.Text("• Coordenadas precisas", size=10),
                    ft.Text("• Enlace a Google Maps", size=10),
                    ft.Text("• Timestamp de envío", size=10)
                ], tight=True),
                actions=[
                    ft.TextButton("📱 WhatsApp", on_click=enviar_whatsapp_con_contacto),
                    ft.TextButton("💬 SMS", on_click=enviar_ubicacion_sms),
                    ft.TextButton("Cancelar", on_click=lambda e: (setattr(dialogo, 'open', False), page.update()))
                ]
            )
            page.dialog = dialogo
            dialogo.open = True
            page.update()
        
        def compartir_ubicacion_sms(e):
            def cerrar_dialogo(e):
                dialogo.open = False
                page.update()
            
            # Simular mensaje SMS
            def enviar_mensaje(e):
                cerrar(e)
                mostrar_snack_bar("📱 Mensaje con ubicación enviado")
            
            def cerrar(e):
                dialogo.open = False
                page.update()
            
            dialogo = ft.AlertDialog(
                title=ft.Text("📱 COMPARTIR UBICACIÓN", color="#1976D2", weight=ft.FontWeight.BOLD),
                content=ft.Column([
                    ft.Text("¿Con quién quieres compartir tu ubicación?", weight=ft.FontWeight.BOLD),
                    ft.Text("• Se enviará un mensaje de texto", size=12, color="#666666"),
                    ft.Text("• Incluye coordenadas GPS", size=12, color="#666666"),
                    ft.Text("• Con enlace a mapa", size=12, color="#666666"),
                    ft.Divider(),
                    ft.Text("Selecciona destinatario:", size=12, color="#666666")
                ], tight=True),
                actions=[
                    ft.TextButton("📞 Mi Familia", on_click=enviar_ubicacion_a_familia),
                    ft.TextButton("🚑 Emergencias", on_click=enviar_mensaje),
                    ft.TextButton("Cancelar", on_click=cerrar_dialogo)
                ]
            )
            page.dialog = dialogo
            dialogo.open = True
            page.update()
        
        def enviar_ubicacion_a_familia(e):
            mostrar_snack_bar("📍 Enviando ubicación a familia...")
        
        def iniciar_prueba_emergencia(e):
            def cerrar_dialogo(e):
                dialogo.open = False
                page.update()
            
            def confirmar_prueba(e):
                dialogo.open = False
                page.update()
                
                # Mostrar simulación
                mostrar_simulacion_sismo()
            
            dialogo = ft.AlertDialog(
                title=ft.Text("🧪 PRUEBA DE EMERGENCIA", color="#FF9800", weight=ft.FontWeight.BOLD),
                content=ft.Text("¿Iniciar simulación completa de sismo?\n\nEsto probará todas las funciones de emergencia."),
                actions=[
                    ft.TextButton("INICIAR PRUEBA", on_click=confirmar_prueba),
                    ft.TextButton("Cancelar", on_click=cerrar_dialogo)
                ]
            )
            page.dialog = dialogo
            dialogo.open = True
            page.update()
        
        def mostrar_simulacion_sismo():
            # Pantalla de simulación
            def cerrar_simulacion(e):
                page.clean()
                page.bgcolor = "#FFFFFF"
                mostrar_menu()
                mostrar_snack_bar("✅ Simulación completada exitosamente")
            
            page.clean()
            page.bgcolor = "#FF5722"
            
            contenido_simulacion = ft.Column([
                ft.Text("🚨", size=80, text_align=ft.TextAlign.CENTER),
                ft.Text("SISMO EN CURSO", size=24, weight=ft.FontWeight.BOLD, color="white", text_align=ft.TextAlign.CENTER),
                ft.Text("MAGNITUD: 6.2", size=20, weight=ft.FontWeight.BOLD, color="#FFEB3B", text_align=ft.TextAlign.CENTER),
                ft.Text("EPICENTRO: 15km sur de CDMX", size=16, color="white", text_align=ft.TextAlign.CENTER),
                ft.Text("🏃‍♂️ AGÁCHATE, CÚBRETSE y SÚJETATE", size=16, color="#FFEB3B", text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD),
                ft.Divider(color="white"),
                ft.Text("🔊 PRUEBA DE ALERTA SONORA", size=14, color="#FFEB3B", weight=ft.FontWeight.BOLD),
                ft.ElevatedButton(
                    "🔊 PROBAR SONIDO",
                    bgcolor="#FFEB3B",
                    color="#D84315",
                    width=200,
                    height=40,
                    on_click=lambda e: mostrar_snack_bar("🔊 Sonido de alerta activado", "#FF9800")
                ),
                ft.ElevatedButton(
                    "✅ FINALIZAR PRUEBA",
                    bgcolor="#4CAF50",
                    color="white",
                    width=250,
                    height=50,
                    on_click=cerrar_simulacion
                )
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
            
            page.add(
                ft.Container(
                    content=contenido_simulacion,
                    alignment=ft.alignment.center,
                    expand=True
                )
            )
            page.update()
        
        titulo = ft.Container(
            content=ft.Text(
                "🆘 EMERGENCIA",
                size=36,
                weight=ft.FontWeight.BOLD,
                color="#FFFFFF",
                text_align=ft.TextAlign.CENTER
            ),
            padding=20
        )
        
        # Botón principal 911
        boton_911 = ft.Container(
            content=ft.ElevatedButton(
                content=ft.Column([
                    ft.Text("📞 LLAMAR 911", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text("Servicios de Emergencia", size=12, opacity=0.8)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, tight=True),
                bgcolor="#FFFFFF",
                color="#B71C1C",
                width=300,
                height=120,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20)),
                on_click=confirmar_llamada_911
            ),
            padding=20
        )
        
        # Otros servicios de emergencia
        otros_servicios = ft.Column([
            ft.Text(
                "UBICACIÓN Y COMUNICACIÓN",
                size=16,
                color="#FFFFFF",
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            ),
            ft.ElevatedButton(
                "📍 Obtener Mi Ubicación",
                bgcolor="#FFFFFF",
                color="#B71C1C",
                width=300,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                on_click=obtener_ubicacion_mejorada
            ),
            ft.ElevatedButton(
                "📱 Enviar por WhatsApp",
                bgcolor="#25D366",
                color="#FFFFFF",
                width=300,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                on_click=enviar_ubicacion_whatsapp
            ),
            ft.ElevatedButton(
                "💬 Compartir por SMS",
                bgcolor="#FFFFFF",
                color="#B71C1C",
                width=300,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                on_click=compartir_ubicacion_sms
            ),
            ft.ElevatedButton(
                "🚒 Bomberos",
                bgcolor="#FFFFFF",
                color="#B71C1C",
                width=300,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                on_click=confirmar_llamada_911
            ),
            ft.ElevatedButton(
                "🚑 Cruz Roja",
                bgcolor="#FFFFFF",
                color="#B71C1C",
                width=300,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                on_click=llamar_cruz_roja
            ),
            ft.ElevatedButton(
                "🏥 Protección Civil",
                bgcolor="#FFFFFF",
                color="#B71C1C",
                width=300,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                on_click=llamar_proteccion_civil
            ),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=8)
        
        # Botón de prueba de emergencia
        boton_prueba = ft.Container(
            content=ft.ElevatedButton(
                content=ft.Column([
                    ft.Text("🧪", size=20),
                    ft.Text("PRUEBA DE", size=12, weight=ft.FontWeight.BOLD),
                    ft.Text("EMERGENCIA", size=12, weight=ft.FontWeight.BOLD)
                ], tight=True),
                bgcolor="#FFEB3B",
                color="#D84315",
                width=120,
                height=80,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                on_click=iniciar_prueba_emergencia
            ),
            alignment=ft.alignment.center
        )
        
        instrucciones = ft.Container(
            content=ft.Column([
                ft.Text(
                    "⚠️ SI ESTÁS ATRAPADO:",
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                ),
                ft.Text("• Golpea 3 veces, pausa, 3 veces (SOS)", size=12, color="#FFFFFF"),
                ft.Text("• Usa un SILBATO si lo tienes", size=12, color="#FFFFFF"),
                ft.Text("• Grita solo si es necesario", size=12, color="#FFFFFF"),
                ft.Text("• Protege boca y nariz del polvo", size=12, color="#FFFFFF"),
                ft.Divider(color="#FFFFFF"),
                ft.Text("📱 COMPARTE TU UBICACIÓN con familiares", size=12, color="#FFEB3B", weight=ft.FontWeight.BOLD)
            ]),
            bgcolor="#424242",
            padding=15,
            border_radius=10
        )
        
        boton_volver = ft.ElevatedButton(
            "← Volver al Menú",
            bgcolor="#424242",
            color="#FFFFFF",
            on_click=lambda e: (setattr(page, 'bgcolor', "#FFFFFF"), volver_menu(e)),
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15))
        )
        
        # Contenedor del botón de prueba
        contenedor_prueba = ft.Container(
            content=ft.Column([
                ft.Text("🧪 PRUEBA DE EMERGENCIA", size=14, color="#FFEB3B", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Text("Simula un sismo para probar la app", size=11, color="white", text_align=ft.TextAlign.CENTER),
                ft.Divider(color="#FFEB3B"),
                boton_prueba
            ]),
            bgcolor="#D84315",
            padding=15,
            border_radius=15,
            border=ft.border.all(3, "#FFEB3B", border_style=ft.border.BorderStyle.DASHED)
        )
        
        page.add(
            ft.Column([
                titulo,
                boton_911,
                otros_servicios,
                contenedor_prueba,
                instrucciones,
                boton_volver
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15, scroll=ft.ScrollMode.AUTO)
        )
        page.update()
    
    # ========== PANTALLA REGISTRAR SISMO ==========
    def pantalla_registrar():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "📝 REGISTRAR SISMO",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        input_magnitud = ft.TextField(
            label="Magnitud (Escala Richter)",
            hint_text="Ej: 5.2",
            keyboard_type=ft.KeyboardType.NUMBER,
            width=350,
            border_radius=10
        )
        
        dropdown_profundidad = ft.Dropdown(
            label="Profundidad",
            options=[
                ft.dropdown.Option("Superficial (0-70km)"),
                ft.dropdown.Option("Intermedio (70-300km)"),
                ft.dropdown.Option("Profundo (>300km)")
            ],
            width=350,
            border_radius=10
        )
        
        input_zona = ft.TextField(
            label="Zona/Epicentro",
            hint_text="Ej: Guerrero, Oaxaca...",
            width=350,
            border_radius=10
        )
        
        input_intensidad = ft.Dropdown(
            label="Intensidad Mercalli Modificada",
            options=[
                ft.dropdown.Option("I - No perceptible"),
                ft.dropdown.Option("II - Muy débil"),
                ft.dropdown.Option("III - Débil"),
                ft.dropdown.Option("IV - Moderado"),
                ft.dropdown.Option("V - Poco fuerte"),
                ft.dropdown.Option("VI - Fuerte"),
                ft.dropdown.Option("VII - Muy fuerte"),
                ft.dropdown.Option("VIII - Severo"),
                ft.dropdown.Option("IX - Violento"),
                ft.dropdown.Option("X - Extremo"),
                ft.dropdown.Option("XI - Casi total"),
                ft.dropdown.Option("XII - Total")
            ],
            width=350,
            border_radius=10
        )
        
        checkbox_sentiste = ft.Checkbox(label="¿Lo sentiste?", value=False)
        checkbox_danos = ft.Checkbox(label="¿Causó daños?", value=False)
        
        def guardar_sismo(e):
            if input_magnitud.value:
                try:
                    magnitud = float(input_magnitud.value)
                    
                    if magnitud < 4.0:
                        nivel = "🟢 SISMO MENOR"
                        desc = "Generalmente no causa daños"
                        color = "#4CAF50"
                    elif magnitud < 5.0:
                        nivel = "🟡 SISMO LIGERO"
                        desc = "Puede causar daños menores"
                        color = "#FFC107"
                    elif magnitud < 6.0:
                        nivel = "🟠 SISMO MODERADO"
                        desc = "Puede causar daños considerables"
                        color = "#FF9800"
                    elif magnitud < 7.0:
                        nivel = "🔴 SISMO FUERTE"
                        desc = "Puede causar daños severos"
                        color = "#F44336"
                    else:
                        nivel = "🔴 SISMO MAYOR"
                        desc = "Puede causar destrucción"
                        color = "#B71C1C"
                    
                    def cerrar(e):
                        dialogo.open = False
                        page.update()
                        # Limpiar campos
                        input_magnitud.value = ""
                        input_zona.value = ""
                        input_intensidad.value = None
                        dropdown_profundidad.value = None
                        checkbox_sentiste.value = False
                        checkbox_danos.value = False
                        page.update()
                    
                    def compartir_sismo(e):
                        cerrar(e)
                        mostrar_snack_bar("📤 Sismo compartido con autoridades", "#2196F3")
                    
                    dialogo = ft.AlertDialog(
                        title=ft.Text("✅ SISMO REGISTRADO", color=color, weight=ft.FontWeight.BOLD),
                        content=ft.Column([
                            ft.Text(f"Nivel: {nivel}", size=16, weight=ft.FontWeight.BOLD),
                            ft.Text(desc),
                            ft.Text(f"Zona: {input_zona.value or 'No especificada'}"),
                            ft.Text(f"Intensidad: {input_intensidad.value or 'No especificada'}"),
                            ft.Divider(),
                            ft.Text("¿Compartir con autoridades?", color="#2196F3")
                        ], tight=True),
                        actions=[
                            ft.TextButton("Compartir", on_click=compartir_sismo),
                            ft.TextButton("Solo Guardar", on_click=cerrar)
                        ]
                    )
                    page.dialog = dialogo
                    dialogo.open = True
                    page.update()
                    
                except:
                    mostrar_snack_bar("❌ Ingresa una magnitud válida", "#D32F2F")
            else:
                mostrar_snack_bar("❌ Por favor ingresa la magnitud", "#D32F2F")
        
        boton_guardar = ft.ElevatedButton(
            content=ft.Column([
                ft.Text("💾", size=20),
                ft.Text("GUARDAR SISMO", weight=ft.FontWeight.BOLD)
            ], tight=True),
            bgcolor="#4CAF50",
            color="#FFFFFF",
            width=350,
            height=60,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
            on_click=guardar_sismo
        )
        
        formulario = ft.Column([
            input_magnitud,
            dropdown_profundidad,
            input_zona,
            input_intensidad,
            checkbox_sentiste,
            checkbox_danos,
            ft.Divider(),
            boton_guardar
        ], spacing=15, scroll=ft.ScrollMode.AUTO)
        
        page.add(
            encabezado,
            ft.Container(content=formulario, padding=20, expand=True)
        )
        page.update()
    
    # ========== PANTALLA KIT DE EMERGENCIA ==========
    def pantalla_kit():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "🎒 KIT DE EMERGENCIA",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        progreso_label = ft.Text(
            "Progreso: 0/15 (0%)",
            size=18,
            weight=ft.FontWeight.BOLD,
            color="#2E7D32"
        )
        
        progreso_container = ft.Container(
            content=ft.Column([
                progreso_label,
                ft.ProgressBar(width=350, height=20, bgcolor="#E0E0E0", color="#4CAF50")
            ], tight=True),
            padding=15,
            bgcolor="#E8F5E9",
            border_radius=10
        )
        
        items_kit_urgentes = [
            "Agua potable (3 litros por persona/día)",
            "Alimentos no perecederos enlatados",
            "Botiquín de primeros auxilios completo",
            "Linterna LED con pilas de repuesto",
            "Radio portátil con pilas",
            "Silbato de emergencia"
        ]
        
        items_kit_importantes = [
            "Medicamentos personales (7 días)",
            "Documentos importantes (identificaciones)",
            "Dinero en efectivo (billetes y monedas)",
            "Herramientas básicas (destornillador, llaves)",
            "Linterna de mano para emergencias",
            "Mascarillas contra polvo"
        ]
        
        items_kit_adicionales = [
            "Llamas y mantas térmicas",
            "Ropa de cambio para 3 días",
            "Artículos de higiene personal",
            "Llaves de repuesto de casa/auto",
            "Mapa de evacuación local",
            "Lista de contactos de emergencia"
        ]
        
        checkboxes_urgentes = []
        checkboxes_importantes = []
        checkboxes_adicionales = []
        
        def actualizar_progreso(e):
            completados = sum(1 for cb in checkboxes_urgentes + checkboxes_importantes + checkboxes_adicionales if cb.value)
            total = len(checkboxes_urgentes) + len(checkboxes_importantes) + len(checkboxes_adicionales)
            porcentaje = (completados / total) * 100
            
            if porcentaje < 30:
                color_progreso = "#F44336"
                estado = "🟢 INICIAL"
            elif porcentaje < 60:
                color_progreso = "#FF9800"
                estado = "🟡 EN PROGRESO"
            elif porcentaje < 100:
                color_progreso = "#4CAF50"
                estado = "🟠 CASI LISTO"
            else:
                color_progreso = "#2196F3"
                estado = "🎉 ¡COMPLETO!"
            
            progreso_label.value = f"Progreso: {completados}/{total} ({porcentaje:.0f}%) - {estado}"
            progreso_label.color = color_progreso
            
            if porcentaje == 100:
                mostrar_snack_bar("🎉 ¡Felicitaciones! Tu kit de emergencia está completo")
            
            page.update()
        
        def crear_item_kit_urgente(texto):
            checkbox = ft.Checkbox(
                label=texto,
                on_change=actualizar_progreso,
                active_color="#F44336"
            )
            checkboxes_urgentes.append(checkbox)
            return checkbox
        
        def crear_item_kit_importante(texto):
            checkbox = ft.Checkbox(
                label=texto,
                on_change=actualizar_progreso,
                active_color="#FF9800"
            )
            checkboxes_importantes.append(checkbox)
            return checkbox
        
        def crear_item_kit_adicional(texto):
            checkbox = ft.Checkbox(
                label=texto,
                on_change=actualizar_progreso,
                active_color="#2196F3"
            )
            checkboxes_adicionales.append(checkbox)
            return checkbox
        
        # Crear secciones del kit
        seccion_urgente = ft.Container(
            content=ft.Column([
                ft.Text("🔴 ARTÍCULOS URGENTES", size=14, weight=ft.FontWeight.BOLD, color="#F44336"),
                ft.Divider(color="#F44336"),
                *[crear_item_kit_urgente(item) for item in items_kit_urgentes]
            ], tight=True),
            bgcolor="#FFEBEE",
            padding=15,
            border_radius=10
        )
        
        seccion_importante = ft.Container(
            content=ft.Column([
                ft.Text("🟡 ARTÍCULOS IMPORTANTES", size=14, weight=ft.FontWeight.BOLD, color="#FF9800"),
                ft.Divider(color="#FF9800"),
                *[crear_item_kit_importante(item) for item in items_kit_importantes]
            ], tight=True),
            bgcolor="#FFF8E1",
            padding=15,
            border_radius=10
        )
        
        seccion_adicional = ft.Container(
            content=ft.Column([
                ft.Text("🔵 ARTÍCULOS ADICIONALES", size=14, weight=ft.FontWeight.BOLD, color="#2196F3"),
                ft.Divider(color="#2196F3"),
                *[crear_item_kit_adicional(item) for item in items_kit_adicionales]
            ], tight=True),
            bgcolor="#E3F2FD",
            padding=15,
            border_radius=10
        )
        
        page.add(
            encabezado,
            progreso_container,
            ft.Container(content=seccion_urgente, padding=15),
            ft.Container(content=seccion_importante, padding=15),
            ft.Container(content=seccion_adicional, padding=15),
        )
        page.update()
    
    # ========== PANTALLA CONTACTOS DE EMERGENCIA ==========
    def pantalla_contactos():
        page.clean()
        
        encabezado = ft.Container(
            content=ft.Row([
                ft.TextButton(
                    "← Volver",
                    style=ft.ButtonStyle(color="#FFFFFF"),
                    on_click=volver_menu
                ),
                ft.Text(
                    "📞 CONTACTOS DE EMERGENCIA",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#FFFFFF"
                )
            ]),
            bgcolor="#C62828",
            padding=10,
            height=70
        )
        
        contactos_lista = []
        
        def crear_tarjeta_contacto(contacto, index):
            def eliminar_contacto(e):
                contactos_lista.remove(contacto)
                actualizar_lista()
                mostrar_snack_bar("🗑️ Contacto eliminado", "#757575")
            
            def llamar_contacto(e):
                mostrar_snack_bar(f"📞 Llamando a {contacto['nombre']}...")
            
            def compartir_ubicacion_contacto(e):
                mostrar_snack_bar(f"📍 Enviando ubicación a {contacto['nombre']}...")
            
            return ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text(f"{index}. {contacto['nombre']}", size=16, weight=ft.FontWeight.BOLD),
                            ft.Container(
                                content=ft.Text("🚨", size=16),
                                padding=5,
                                bgcolor="#F44336",
                                border_radius=5
                            )
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text(f"📱 {contacto['telefono']}", size=14),
                        ft.Text(f"👤 {contacto['relacion']}", size=12, color="#666666"),
                        ft.Row([
                            ft.ElevatedButton(
                                "📞 Llamar",
                                bgcolor="#4CAF50",
                                color="white",
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                                on_click=llamar_contacto
                            ),
                            ft.ElevatedButton(
                                "📍 Ubicación",
                                bgcolor="#2196F3",
                                color="white",
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                                on_click=compartir_ubicacion_contacto
                            ),
                            ft.ElevatedButton(
                                "🗑️",
                                bgcolor="#757575",
                                color="white",
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                                on_click=eliminar_contacto
                            )
                        ], spacing=5)
                    ], tight=True),
                    padding=15,
                    width=350
                ),
                elevation=3,
                color="#FFEBEE"
            )
        
        lista_contactos_container = ft.Container(
            content=ft.Text(
                "No hay contactos guardados",
                size=14,
                color="#616161",
                text_align=ft.TextAlign.CENTER
            ),
            padding=15,
            expand=True
        )
        
        def actualizar_lista():
            if contactos_lista:
                contenido = ft.Column([
                    ft.Text("📞 CONTACTOS DE EMERGENCIA", size=16, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                    ft.Divider(),
                    *[crear_tarjeta_contacto(contacto, i+1) for i, contacto in enumerate(contactos_lista)]
                ], spacing=10, scroll=ft.ScrollMode.AUTO)
                lista_contactos_container.content = contenido
            else:
                lista_contactos_container.content = ft.Text(
                    "No hay contactos guardados",
                    size=14,
                    color="#616161",
                    text_align=ft.TextAlign.CENTER
                )
            page.update()
        
        input_nombre = ft.TextField(
            label="Nombre completo",
            width=350,
            border_radius=10
        )
        
        input_telefono = ft.TextField(
            label="Teléfono (10 dígitos)",
            keyboard_type=ft.KeyboardType.PHONE,
            width=350,
            border_radius=10
        )
        
        input_relacion = ft.TextField(
            label="Relación (familiar/amigo/trabajo)",
            width=350,
            border_radius=10
        )
        
        def agregar_contacto(e):
            if input_nombre.value and input_telefono.value:
                if len(input_telefono.value) == 10 and input_telefono.value.isdigit():
                    contacto = {
                        "nombre": input_nombre.value,
                        "telefono": input_telefono.value,
                        "relacion": input_relacion.value or "No especificada"
                    }
                    contactos_lista.append(contacto)
                    
                    # Limpiar campos
                    input_nombre.value = ""
                    input_telefono.value = ""
                    input_relacion.value = ""
                    
                    actualizar_lista()
                    
                    mostrar_snack_bar("✅ Contacto agregado exitosamente")
                else:
                    mostrar_snack_bar("❌ El teléfono debe tener exactamente 10 dígitos", "#D32F2F")
            else:
                mostrar_snack_bar("❌ Completa nombre y teléfono", "#D32F2F")
        
        # Agregar contactos de emergencia predefinidos
        contactos_predefinidos = [
            {"nombre": "911 Emergencias", "telefono": "9110000000", "relacion": "Servicios de Emergencia"},
            {"nombre": "Cruz Roja Mexicana", "telefono": "5551234567", "relacion": "Cruz Roja"},
            {"nombre": "Protección Civil CDMX", "telefono": "5551234568", "relacion": "Protección Civil"}
        ]
        
        # Solo agregar si no hay contactos
        if not contactos_lista:
            contactos_lista.extend(contactos_predefinidos)
        
        formulario = ft.Container(
            content=ft.Column([
                ft.Text("➕ Agregar Nuevo Contacto", weight=ft.FontWeight.BOLD, size=16, text_align=ft.TextAlign.CENTER),
                input_nombre,
                input_telefono,
                input_relacion,
                ft.ElevatedButton(
                    content=ft.Column([
                        ft.Text("➕", size=16),
                        ft.Text("Agregar Contacto", weight=ft.FontWeight.BOLD)
                    ], tight=True),
                    bgcolor="#4CAF50",
                    color="#FFFFFF",
                    width=350,
                    height=60,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                    on_click=agregar_contacto
                )
            ], spacing=10),
            bgcolor="#F5F5F5",
            padding=15,
            border_radius=10
        )
        
        page.add(
            encabezado,
            ft.Container(content=formulario, padding=15),
            lista_contactos_container
        )
        
        actualizar_lista()
        page.update()
    
    # ========== INICIAR APP ==========
    mostrar_menu()
# Ejecutar la app
if __name__ == "__main__":
    ft.app(target=main)
