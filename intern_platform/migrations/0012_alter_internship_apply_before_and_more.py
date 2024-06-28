import datetime
from django.db import migrations, models

def set_defaults(apps, schema_editor):
    Internship = apps.get_model('intern_platform', 'Internship')
    today = datetime.date.today()
    Internship.objects.filter(apply_before__isnull=True).update(apply_before=today)
    Internship.objects.filter(end_date__isnull=True).update(end_date=today)
    Internship.objects.filter(start_date__isnull=True).update(start_date=today)
    Internship.objects.filter(internship_country__isnull=True).update(internship_country='INDIA')

class Migration(migrations.Migration):

    dependencies = [
        ('intern_platform', '0011_alter_internship_apply_before_and_more'),
    ]

    operations = [
        # Step 1: Alter the fields to allow nulls temporarily
        migrations.AlterField(
            model_name='internship',
            name='apply_before',
            field=models.DateField(null=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='internship',
            name='end_date',
            field=models.DateField(null=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='internship',
            name='start_date',
            field=models.DateField(null=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='internship',
            name='internship_country',
            field=models.CharField(max_length=255, null=True, default='INDIA'),
        ),

        # Step 2: Populate the fields with default values
        migrations.RunPython(set_defaults),

        # Step 3: Alter the fields to be non-nullable
        migrations.AlterField(
            model_name='internship',
            name='apply_before',
            field=models.DateField(null=False, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='internship',
            name='end_date',
            field=models.DateField(null=False, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='internship',
            name='start_date',
            field=models.DateField(null=False, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='internship',
            name='internship_country',
            field=models.CharField(max_length=255, null=False, default='INDIA'),
        ),
    ]
