from django.contrib import admin
from .models import Company, Device, Employee, DeviceAssignment

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'company', 'condition', 'checkout')
    list_filter = ('company', 'condition', 'checkout')
    search_fields = ('name', 'serial_number')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'company')
    list_filter = ('company',)
    search_fields = ('user__username',)


@admin.register(DeviceAssignment)
class DeviceAssignmentAdmin(admin.ModelAdmin):
    list_display = ('device', 'employee', 'assigned_date', 'return_date')
    list_filter = ('device', 'employee', 'assigned_date', 'return_date')
    search_fields = ('device__name', 'employee__user__username')
