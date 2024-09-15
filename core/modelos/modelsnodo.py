from django.db import models


COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK') )

class ClaseNodo(models.Model):
    llave = models.CharField(max_length=50, default="llave1")
    model = models.CharField(max_length=50, default="modelo1")
    grupo = models.IntegerField(default=2)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default="GREEN")

    def __str__(self):
        return self.llave
    

class ClaseCBROperacion(models.Model):
    timestamp = models.DateTimeField()
    operacion = models.CharField(max_length=50, default="open")
    id_nodo = models.IntegerField(default=2)
    # id_nodo = models.IntegerField(default=2) deltaT para calcular el delta

    def __str__(self):
        return self.id_nodo

class ClaseOperacionTransiente(models.Model):
    delta = models.IntegerField()
    aper1 = models.FloatField()
    fasea = models.FloatField()
    a52 = models.BooleanField()

    def __str__(self):
        return self.delta