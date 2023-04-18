from django.contrib import admin
from parkingapp.models import Add,Exit,Feedback
# Register your models here.

#admin.site.register(Add)

class AddAdmin(admin.ModelAdmin):
    list_display=['token','Name','phone','v_type','v_number','payment','Created_on','uid']

    list_filter=['v_type','payment','Created_on']


#register modeladmin  class with model

admin.site.register(Add ,AddAdmin)
admin.site.site_header="Online Parking Register"
admin.site.site_title="OPR Admin"
admin.site.index_title="OPR"

'''
class ExitAdmin(admin.ModelAdmin):
    list_display=['token','Name','phone','v_type','v_number','payment','Created_on']
'''

class FeedAdmin(admin.ModelAdmin):
    list_display=['Name','E_mail','sub','msg','Created_on']
    list_filter=['Created_on']

admin.site.register(Feedback,FeedAdmin)