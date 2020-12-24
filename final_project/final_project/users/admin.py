from django.contrib import admin
from django.utils.html import format_html

from .models import SiteUser
from django.urls import path, reverse
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect


class UserAdmin(admin.ModelAdmin):
    change_list_template = "button.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('login/', auth_views.LoginView.as_view(), {'next_page': 'login'}),
            path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'index'})

        ]

        return my_urls + urls


admin.site.register(SiteUser, UserAdmin)
