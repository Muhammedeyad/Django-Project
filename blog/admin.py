from django.contrib import admin
from .models import post, Category, Bikes
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')
    list_filter = ('catagory', 'created_at')
    


admin.site.register(post, PostAdmin)
admin.site.register(Category)
admin.site.register(Bikes)