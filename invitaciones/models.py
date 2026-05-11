from django.db import models

class Invitacion(models.Model):
    FONT_CHOICES = [
        ('Inter', 'Inter (Limpio y Moderno)'),
        ('Playfair Display', 'Playfair Display (Elegante y Clásico)'),
        ('Nunito', 'Nunito (Redondeado y Amigable)'),
        ('Pacifico', 'Pacifico (Cursiva Juguetona)'),
        ('Cinzel', 'Cinzel (Sofisticado Serif)'),
    ]

    slug = models.SlugField(unique=True, help_text="URL única para la invitación (ej: baby-shower-mateo)")
    titulo_landing = models.CharField(max_length=200, help_text="Ej: ¡Bienvenido Mateo!")
    descripcion = models.TextField(help_text="Texto de bienvenida o dedicatoria")
    fecha_evento = models.DateTimeField()
    direccion_texto = models.CharField(max_length=255, help_text="Ej: Calle Falsa 123, Ciudad")
    direccion_google_maps_link = models.URLField(help_text="Link directo para abrir en Google Maps")
    link_lista_deseos = models.URLField(blank=True, null=True, help_text="Link a la mesa de regalos (opcional)")

    # Apariencia
    color_primario = models.CharField(max_length=7, default="#8b5cf6", help_text="Color para botones y acentos")
    color_texto = models.CharField(max_length=7, default="#ffffff", help_text="Color del texto principal")
    fuente_texto = models.CharField(max_length=50, choices=FONT_CHOICES, default="Inter", help_text="Tipografía para la invitación")

    # Controles Avanzados 3D
    fuerza_giro = models.FloatField(default=1.0, help_text="Multiplicador de la rotación 3D (Ej: 1.0 normal, 0.5 suave)")
    fuerza_desplazamiento = models.FloatField(default=1.0, help_text="Multiplicador del deslizamiento (Ej: 1.0 normal, 2.0 agresivo)")
    activar_bokeh = models.BooleanField(default=False, help_text="Activar efecto cinematográfico de desenfoque de profundidad")

    def __str__(self):
        return self.titulo_landing

class CapaParallax(models.Model):
    DISPOSITIVO_CHOICES = [
        ('todos', 'Ambos (Universal)'),
        ('movil', 'Solo Móvil (Vertical 9:16)'),
        ('escritorio', 'Solo Escritorio (Horizontal 16:9)'),
    ]

    invitacion = models.ForeignKey(Invitacion, related_name='capas', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='parallax/', help_text="Sube una imagen (idealmente PNG transparente para capas frontales)")
    z_index = models.IntegerField(default=0, help_text="Posición Z de la capa (Ej: -5 para fondo, 0 medio, 5 frente). Determina la escala y el nivel de parallax.")
    orden = models.PositiveIntegerField(default=0, help_text="Orden en el que se renderiza (0 primero, 1 segundo...)")
    
    dispositivo = models.CharField(max_length=20, choices=DISPOSITIVO_CHOICES, default='todos', help_text="¿En qué pantallas debe mostrarse esta capa?")
    pegar_abajo = models.BooleanField(default=False, help_text="Si se activa, la imagen no volará hacia arriba con el giroscopio, ocultando el corte del borde inferior.")

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"Capa {self.orden} de {self.invitacion.titulo_landing}"
