from django.contrib import admin
from .models import Ticket, Review


class ReviewInline(admin.StackedInline):
    """Rattachement de la critique au ticket dans l'interface d'administration."""
    model = Review
    extra = 0
    fields = ('ticket', 'headline', 'rating', 'body', 'author', 'time_created')
    readonly_fields = ('time_created',)


class TicketAdmin(admin.ModelAdmin):
    """Gestion du ticket dans l'interface d'administration."""
    inlines = [ReviewInline,]
    list_display = ('title', 'author', 'time_created', 'image', 'description')
    readonly_fields = ('time_created',)


class ReviewAdmin(admin.ModelAdmin):
    """Gestion autonome de la critique dans l'interface d'administration."""
    list_display = ('ticket', 'author', 'time_created', 'headline', 'rating', 'body')
    readonly_fields = ('time_created',)


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
