from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="home"),

    path("signin/", views.signin, name="signin"),

    path("signup/", views.signup, name="signup"),

    path("signout/", views.signout, name="signout"),

    path("restaurant/<int:id>/", views.restaurant_menu),

    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),

    path('cart/', views.cart, name='cart'),

    path('remove-from-cart/<int:index>/', views.remove_from_cart),

    path('increase/<int:item_id>/', views.increase_quantity),

    path('decrease/<int:item_id>/', views.decrease_quantity),

    path('checkout/', views.checkout),

    path('order-success/', views.order_success),

    path('my-orders/', views.my_orders),
]


