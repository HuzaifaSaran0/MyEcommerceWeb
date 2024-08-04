from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="search"),
    path("product_view/<int:myid>", views.product_view, name="product"),
    path("checkout/", views.checkout, name="Checkout"),
    path("login/", views.loginPage, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_page, name="logout")
]
