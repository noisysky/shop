from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    count = models.PositiveIntegerField()
    type = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')  # install pillow for use ImageField (pip install pillow)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

#    @property
#    def total(self):
#        return self.price * self.count
