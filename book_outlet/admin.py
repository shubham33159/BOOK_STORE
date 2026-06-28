from django.contrib import admin
from book_outlet.models import Book, Author, Address, Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author","rating",)
    list_display = ("title","rating","author")

    # list_display = ("title","rating","author__first_name", "author__last_name")

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
