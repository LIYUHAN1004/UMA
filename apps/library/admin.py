from django.contrib import admin
from .models import Book
from .models import BookDetail
from .models import Publisher

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')  # 列表顯示欄位
    list_filter = ('author',)  # 篩選器
    search_fields = ('title', 'author')  # 搜尋欄位
    ordering = ('-price',)  # 預設排序

@admin.register(BookDetail)
class BookDetailAdmin(admin.ModelAdmin):
    list_display = ('book', 'isbn', 'publisher', 'publish_date', 'pages', 'description', 'cover_image')  # 列表顯示欄位
    list_filter = ('publisher',)  # 篩選器
    search_fields = ('book__title', 'isbn')  # 搜尋欄位
    ordering = ('-publish_date',)  # 預設排序

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')  # 列表顯示欄位
    search_fields = ('name', 'city')  # 搜尋欄位
    ordering = ('name',)  # 預設排序