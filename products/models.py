import os
from django.db import models
from django.dispatch import receiver
from django.core.validators import MinValueValidator


# class Category(models.Model):
#   name = models.CharField(max_length=250)

#   def __str__(self):
#     return self.name


# class Seller(models.Model):
#   name = models.CharField(max_length=250)

#   def __str__(self):
#     return self.name


class Product(models.Model):
  title = models.CharField(max_length=250)
  singular_price = models.FloatField(validators=[MinValueValidator(0)])
  plural_price = models.FloatField(validators=[MinValueValidator(0)])
  photo = models.ImageField(null=True, upload_to='uploads/products')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  def __str__(self):
    return self.title


@receiver(models.signals.pre_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
  """
    Deletes file from filesystem
    when corresponding `Order` object is deleted.
  """
  if instance.photo:
    if os.path.isfile(instance.photo.path):
      os.remove(instance.photo.path)

@receiver(models.signals.pre_save, sender=Product)
def auto_delete_file_on_chagne(sender, instance, **kwargs):
  """
  Deletes old file from filesystem
  when corresponding `Order` object is updated
  with new file.
  """
  if not instance.pk:
      return False
  try:
    old_photo = Product.objects.get(pk=instance.pk).photo
  except Product.DoesNotExist:
    return False

  new_photo = instance.photo
  if not old_photo == new_photo:
    if os.path.isfile(old_photo.path):
      os.remove(old_photo.path)
