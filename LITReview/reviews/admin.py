from django.contrib import admin
from .models import Ticket, Review


class ReviewInline(admin.TabularInline):
    model = Review
    fields = ('ticket', 'headline', 'rating', 'body', 'user', 'time_created')
    readonly_fields = ('time_created',)


class TicketAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ('title', 'user', 'time_created', 'image', 'description')
    search_fields = ['title']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'user', 'time_created', 'headline', 'rating', 'body')
    search_fields = ['ticket__title']


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
