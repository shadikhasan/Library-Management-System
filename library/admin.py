from django.contrib import admin
from django.utils.translation import gettext as _
# Register your models here.
from .models import *


admin.site.register(Book)
admin.site.register(Bill)
admin.site.register(Rating)
admin.site.register(Category)

@admin.register(Ebook)
class EbookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'file_format') 

@admin.register(BookNote)
class BookNoteAdmin(admin.ModelAdmin):
    list_display = ('username', 'book_name', 'note', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'book__name', 'note')
    ordering = ('-created_at',)

    def username(self, obj):
        return obj.user.username

    username.admin_order_field = 'user__username'
    username.short_description = 'User'

    def book_name(self, obj):
        return obj.book.name

    book_name.admin_order_field = 'book__name'
    book_name.short_description = 'Book Name'

    def created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M:%S")

    created_at.admin_order_field = 'created_at'
    created_at.short_description = 'Created At'

# class BillAdmin(admin.ModelAdmin):
#     pass
#     # list_display = ['id','user', 'amount', 'reason', 'isActive' ]
#     # list_editable = ['isActive']
#     # list_filter = ['isActive',]
#     # search_fields = ['user__username']
#     # readonly_fields = [ 'user', 'amount', 'reason', 'reservation']

# admin.site.register(Bill, BillAdmin)


class ReservationAdmin(admin.ModelAdmin):

    list_display = ['id', 'book', 'user', 'status']
    list_editable = ['status']
    list_filter = ['status',]
    search_fields = ['book__name', 'user__username']
    readonly_fields = ['requested_at', 'reserved_at',
                       'expected_return_date', 'isActive']
    fieldsets = (
        (None, {'fields': ('book', 'user')}),
        (_('Other Info'),
            {
                'fields': (
                    'requested_at',
                    'reserved_at',
                    'expected_return_date',
                    'isActive'
                )
        }
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('book', 'user')
        }),
    )


admin.site.register(Reservation, ReservationAdmin)
