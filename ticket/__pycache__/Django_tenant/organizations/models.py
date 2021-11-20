from django.db import models
from tenant_schemas.models import TenantMixin
# Create your models here.
class Organization(TenantMixin):
    name = models.CharField(max_length=100)
