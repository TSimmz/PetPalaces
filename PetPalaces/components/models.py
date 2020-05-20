from django.db import models

# Create your models here.
class Components(models.Model):
    x_dim = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    y_dim = models.DecimalField(null=True,decimal_places=2, max_digits=5)
    z_dim = models.DecimalField(null=True,decimal_places=2, max_digits=5)
    summary= models.TextField(blank=True, null=True)