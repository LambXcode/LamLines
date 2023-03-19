from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from django.contrib.auth.models import User

# Register your models here.
class FlightAdmin(admin.ModelAdmin):   #lets see more info of a flight 
    list_display = ("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin): #lets see more info of a passenger
    filter_horizontal = ("flights",)

admin.site.site_url = '/users/login'

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register the UserProfile model with its admin interface
admin.site.register(UserProfile)
