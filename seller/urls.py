from django.urls import path
from.import views
app_name= 'seller'
urlpatterns = [
    path('seller/', views.seller, name= 'seller'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addproduct/',views.addproduct, name='addproduct'),
    path('viewproduct/', views.viewproduct, name='viewproduct'),
    path('signup/', views.signup, name='signup'),
    path('delete_pdt/<int:product_id>', views.delete_pdt, name='delete_pdt'),
    path('update_pdt/<int:product_id>', views.update_pdt, name='update_pdt'),
    path('logout/',views.logout, name='logout')

]