from django.contrib import admin
from .models import Member
from import_export.admin import ImportExportModelAdmin
#from django.contrib import admin



# Register your models here.
@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    pass