from django.urls import path
from.import views
app_name= 'customer'
urlpatterns = [
    path ('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('products/', views.products, name='products'),
    path('logout/',views.logout, name='logout'),
    path('add_to_cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('remove_cart/<int:product_id>', views.remove_cart, name='remove_cart'),
    path('pay_cart/', views.pay_cart, name='pay_cart'),
    path('search/', views.search, name='search')
]