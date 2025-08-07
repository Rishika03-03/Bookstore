from django.contrib import admin
from django.urls import path
from store import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login_view),  # Redirect root
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('home/categories/', views.category_view, name='category_view'),  # ✅ This must exist
    path('home/categories/action/', views.action_view, name='action'),
    path('home/categories/fictional/', views.fictional_view, name='fictional'),
    path('home/categories/comedy/', views.comedy_view, name='comedy'),
    path('home/categories/horror/', views.horror_view, name='horror'),
    path('home/categories/motivational/', views.motivational_view, name='motivational'),
    path('home/categories/thriller/', views.thriller_view, name='thriller'),
    path('cart/', views.cart_view, name='cart'),
    path('buynow/', views.buy_now, name='buy_now'),
    path('myaccount/', views.my_account, name='my_account'),
    path('logout/', views.logout_view, name='logout'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path("orders/", views.my_orders, name="orders"),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('help/', views.help_page, name='help'),
    
    
]
