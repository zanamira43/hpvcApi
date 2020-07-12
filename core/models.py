import os
import random, string
# import uuid
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings

# def upload_image_file_path(instance, filename):
#   """Generate file path or new recipe image"""
#   ext = filename.split('.')[-1]
#   filename = f"{uuid.uuid4()}.{ext}"
#   return os.path.join('uploads/orders', filename)

def rand_slug():
  return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
  
class UserManager(BaseUserManager):
  
  def create_user(self, email, password=None, **extra_fields):
    """creates and saves a new user"""
    
    if not email:
      raise ValueError('Users muste have email address')
    user = self.model(email=self.normalize_email(email), **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    
    return user
  
  def create_superuser(self, email, password):
    """creates and saves a new superuser"""
    user = self.create_user(email, password)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    
    return user


class User(AbstractBaseUser, PermissionsMixin):
  """Custom user model that supports using email instead of username"""
  email = models.EmailField(max_length=200, unique=True)
  name = models.CharField(max_length=200)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  
  

  USERNAME_FIELD = 'email'
  
  objects = UserManager()
  
  
  def __str__(self):
    return self.email
  
  
  
class Order(models.Model):
  """Order Model"""
  name = models.CharField(max_length=200, null=True, blank=True)
  slug = models.CharField(max_length=255, default=rand_slug(), unique=True, blank=True, null=True)
  # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=0)
  rquantity = models.IntegerField(default=0)
  price = models.FloatField(default=00.0)
  description = models.TextField(blank=True, null=True)
  image = models.ImageField(null=True, upload_to='uploads/orders')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  accepted = models.BooleanField(default=False)
  received = models.BooleanField(default=False)
  
  def __str__(self):
    return self.name

@receiver(models.signals.pre_delete, sender=Order)
def auto_delete_file_on_delete(sender, instance, **kwargs):
  """
    Deletes file from filesystem
    when corresponding `Order` object is deleted.
  """
  if instance.image:
    if os.path.isfile(instance.image.path):
      os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=Order)
def auto_delete_file_on_chagne(sender, instance, **kwargs):
  """
  Deletes old file from filesystem
  when corresponding `Order` object is updated
  with new file.
  """
  if not instance.pk:
      return False
  try:
    old_image = Order.objects.get(pk=instance.pk).image
  except Order.DoesNotExist:
    return False
  
  new_image = instance.image
  if not old_image == new_image:
    if os.path.isfile(old_image.path):
      os.remove(old_image.path)


class Transfer(models.Model):
  """transfer Model"""
  by_who = models.CharField(max_length=100)
  for_who = models.CharField(max_length=100)
  amount = models.FloatField(default=00.0)
  transfer_date = models.DateField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.amount
  