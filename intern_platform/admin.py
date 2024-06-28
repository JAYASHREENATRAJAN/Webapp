import csv
import pandas as pd
from django.http import HttpResponse
from django.contrib import admin
from .models import CustomUser, InternProfile, EmployerProfile, Internship, Application

# Define export functions
def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta}.csv'
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])

    return response

export_as_csv.short_description = "Export Selected as CSV"

def export_as_excel(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    data = []
    for obj in queryset:
        # Convert timezone-aware datetimes to timezone-unaware datetimes
        obj_data = [getattr(obj, field) for field in field_names]
        data.append([val.replace(tzinfo=None) if hasattr(val, 'tzinfo') else val for val in obj_data])

    df = pd.DataFrame(data, columns=field_names)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'
    df.to_excel(response, index=False)

    return response

export_as_excel.short_description = "Export Selected as Excel"

# Define model admin classes with export actions
class CustomUserAdmin(admin.ModelAdmin):
    actions = [export_as_csv, export_as_excel]

class InternProfileAdmin(admin.ModelAdmin):
    actions = [export_as_csv, export_as_excel]

class EmployerProfileAdmin(admin.ModelAdmin):
    actions = [export_as_csv, export_as_excel]

class InternshipAdmin(admin.ModelAdmin):
    actions = [export_as_csv, export_as_excel]

class ApplicationAdmin(admin.ModelAdmin):
    actions = [export_as_csv, export_as_excel]

# Register models with custom admin classes
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(InternProfile, InternProfileAdmin)
admin.site.register(EmployerProfile, EmployerProfileAdmin)
admin.site.register(Internship, InternshipAdmin)
admin.site.register(Application, ApplicationAdmin)
