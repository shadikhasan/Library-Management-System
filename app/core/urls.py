"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from authentication.views import register, user_login, user_logout
# from event.views import EventList, EventDetail, RegistrationList, RegistrationDetail
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),

    path('books/<int:book_id>', book_details, name='book_detail'),
    path('books/<int:book_id>/reservation', reserve_book, name='reserve_book'),
    path('books/<int:book_id>/rating', give_rating, name='give_rating'),

    path('myrequests/', myrequests, name='myrequests'),
    path('myrequests/<int:reservation_id>/cancel',
         cancel_reservation, name='cancel_reservation'),
    path('myrequests/<int:reservation_id>/lost', lost_book, name='lost_book'),

    path('mybills/', my_bill, name='my_bill'),
    path('mybills/<int:bill_id>/pay', pay_bill, name='pay_bill'),

    path('my-notebook/', my_notebook, name='my_notebook'),
    path('add-note/', add_note, name='add_note'),
    path('edit_note/<int:note_id>/', edit_note, name='edit_note'),
    path('delete_note/<int:note_id>/', delete_note, name='delete_note'),
    
    path('ebooks/', ebook_list, name='ebook_list'),
    path('ebooks/<int:ebook_id>/', read_ebook, name='read_ebook'),
    
    path('', dashboard, name='dashboard'),


    # path('api/events/', EventList.as_view(), name='event-list'),
    # path('api/events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    # path('api/registrations/', RegistrationList.as_view(), name='registration-list'),
    # path('api/registrations/<int:pk>/', RegistrationDetail.as_view(), name='registration-detail'),
]


# if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
