# Generated by Django 5.0.3 on 2024-04-30 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_alter_driverlicense_driver_license_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='Address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='City',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='Email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='Phone_Number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='State',
            field=models.CharField(blank=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('AS', 'American Samoa'), ('DC', 'District of Columbia'), ('FM', 'Federated States of Micronesia'), ('GU', 'Guam'), ('MH', 'Marshall Islands'), ('MP', 'Northern Mariana Islands'), ('PW', 'Palau'), ('PR', 'Puerto Rico'), ('VI', 'Virgin Islands'), ('AE', 'Armed Forces Africa'), ('AA', 'Armed Forces Americas (except Canada)'), ('AE', 'Armed Forces Canada'), ('AE', 'Armed Forces Europe'), ('AE', 'Armed Forces Middle East'), ('AP', 'Armed Forces Pacific')], max_length=2, null=True),
        ),
    ]