from django.db import models

# Area Equipos

class Equipo(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=50)
    propietario = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        abstract = True

class Laptop(Equipo):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    tamano_pantalla = models.DecimalField(max_digits=5, decimal_places=2)
    procesador = models.CharField(max_length=100)
    generacion = models.CharField(max_length=50)
    memoria_ram = models.IntegerField()
    tipo_ram = models.CharField(max_length=50)
    bus_ram = models.CharField(max_length=50)
    tarjeta_grafica = models.CharField(max_length=100)
    capacidad_tarjeta_grafica = models.IntegerField()
    disco_hdd = models.IntegerField()
    disco_ssd = models.IntegerField()
    serial_cargador = models.CharField(max_length=100)
    marca_cargador = models.CharField(max_length=100)

class PC(Equipo):
    marca = models.CharField(max_length=100)
    procesador = models.CharField(max_length=100)
    generacion = models.CharField(max_length=50)
    memoria_ram = models.IntegerField()
    tipo_ram = models.CharField(max_length=50)
    bus_ram = models.CharField(max_length=50)
    tarjeta_grafica = models.CharField(max_length=100)
    capacidad_tarjeta_grafica = models.IntegerField()
    disco_hdd = models.IntegerField()
    disco_ssd = models.IntegerField()

class Celular(Equipo):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    procesador = models.CharField(max_length=100)
    memoria_ram = models.IntegerField()
    almacenamiento = models.IntegerField()
    pantalla = models.DecimalField(max_digits=5, decimal_places=2)
    bateria = models.IntegerField()

class Accesorio(models.Model):
    equipo_laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, null=True, blank=True, related_name='accesorios')
    equipo_pc = models.ForeignKey(PC, on_delete=models.CASCADE, null=True, blank=True, related_name='accesorios')
    equipo_celular = models.ForeignKey(Celular, on_delete=models.CASCADE, null=True, blank=True, related_name='accesorios')
    tamano_monitor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    modelo_monitor = models.CharField(max_length=100, null=True, blank=True)
    modelo_teclado = models.CharField(max_length=100, null=True, blank=True)
    modelo_mouse = models.CharField(max_length=100, null=True, blank=True)

# Area Persona

class Persona(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    correo = models.EmailField()
    numero_celular = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

# Area Entrega

class Asignacion(models.Model):
    dni = models.ForeignKey(Persona, on_delete=models.CASCADE)
    equipo_laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, null=True, blank=True)
    equipo_pc = models.ForeignKey(PC, on_delete=models.CASCADE, null=True, blank=True)
    equipo_celular = models.ForeignKey(Celular, on_delete=models.CASCADE, null=True, blank=True)
    fecha_entrega = models.DateField()
    estado_maquina_entrega = models.CharField(max_length=100)

    def __str__(self):
        return f"Asignación de equipo a {self.dni}"

class Devolucion(models.Model):
    asignacion = models.OneToOneField(Asignacion, on_delete=models.CASCADE)
    fecha_devolucion = models.DateField()
    estado_maquina_devolucion = models.CharField(max_length=100)

    def __str__(self):
        return f"Devolución de equipo por {self.asignacion.dni}"
