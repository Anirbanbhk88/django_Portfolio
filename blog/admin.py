from django.contrib import admin
from blog.models import Post, Category

'''
connect the model classes to the admin class
'''
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)