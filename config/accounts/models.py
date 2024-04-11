from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

# class User(AbstractUser):
#     class Meta:
#         permissions = (
#             # Vehicles CRUD
#             ('create_vehicle', 'Can create a new vehicle')
#             ('view_vehicle', 'Can view vehicle in details'),
#             ('edit_vehicle', 'Can edit vehicle details'),
#             ('delete_vehicle', 'Can delete a vehicle')
#             ('assign_trip', 'Can assign trips to drivers'),
#         )

#         USER_TYPES = (
#             ('driver','Driver'),
#             ('dispatcher','Dispatcher'),
#             ('manager','Manager'),
#             ('admin','Admin'),
#         )
#         user_type = models.Charfield(max_length=20, choices=USER_TYPES)