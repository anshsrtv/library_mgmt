from django.contrib import admin
from django.urls import path
from core import views
from librarian import views as libviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello, name='hello'),
    path('list_guests/', views.show_guests, name='show_guests'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_student/', libviews.add_student, name="add_student" ),
    path('add_book/', libviews.add_book, name="add_book"),
    path('update_student/<int:student_id>/', libviews.update_student, name="update_student" ),
    path('update_book/<int:book_id>/', libviews.update_book, name="update_book"),
    path('delete_student/<int:student_id>/', libviews.delete_student, name="delete_student" ),
    path('delete_book/<int:book_id>/', libviews.delete_book, name="delete_book"),
    path('add_lib/<int:profile_id>/', views.add_librarian, name='add_lib'),
    path('delete_lib/<int:profile_id>/', views.delete_librarian, name='delete_lib'),
    path('issue/<int:book_id>/', libviews.issue_book, name='issue'),
    path('return/<int:book_id>/', libviews.return_book, name='return'),
    path('view_issued/', libviews.view_issued_books, name='view_issued'),
    path('view_issued/<int:student_id>/', libviews.student_issued_books, name='student_issued_books'),
    path('register_lib/', views.register_lib, name='register_lib'),
]