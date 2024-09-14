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
        return self.id
    
