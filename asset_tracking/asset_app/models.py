from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=11, unique = True)
    email = models.EmailField(max_length=250)
    
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ('name',)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True) 
    serial_number = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="devices")
    condition = models.CharField(max_length=220, default="Good")
    checkout = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        ordering = ['serial_number',]
    
    def __str__(self):
        return self.name
        

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employe")
    devices = models.ManyToManyField(Device)
    
    def __str__(self):
        return self.user.username


class DeviceAssignment(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='assignments')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assignments')
    updated_at = models.DateField(auto_now_add=True)
    assigned_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    
    class Meta:
        verbose_name = 'DeviceAssignment'
        ordering = ('-updated_at',)
        
    def __str__(self):
        return f"Assignment: {self.device.name} to {self.employee.user.username}"
    
    