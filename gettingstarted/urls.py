from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import banking.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("banks/ifsc/<str:ifsc>/", banking.views.get_bank_detials_from_ifsc_code, name="bank_from_ifsc_code"),
    path("bankdetails/nameandcity/", banking.views.get_bank_detials_from_name_and_city, name="get_bank_detials_from_name_and_city"),
    path("index/", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
