from django.contrib import admin
from .models import ProjectSRC, ProjectBinary


admin.site.register(ProjectBinary)
admin.site.register(ProjectSRC)
