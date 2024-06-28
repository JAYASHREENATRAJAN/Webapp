# Generated by Django 4.2.3 on 2024-05-11 07:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('intern_platform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_employer',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_intern',
        ),
        migrations.RemoveField(
            model_name='internship',
            name='duration',
        ),
        migrations.AddField(
            model_name='application',
            name='cover_letter',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='application',
            name='submitted_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('intern', 'Intern'), ('employer', 'Employer')], default='intern', max_length=20),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='company_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='company_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='employerprofile',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='internprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='internprofile',
            name='resume',
            field=models.FileField(blank=True, upload_to='resumes/'),
        ),
        migrations.AddField(
            model_name='internprofile',
            name='skills',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='internship',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='internship',
            name='industry',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='internship',
            name='skills_preferred',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='internship',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='internship',
            name='stipend',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], max_length=20),
        ),
    ]
