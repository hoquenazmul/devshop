from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path("products/", views.product_list),
    path("products/<int:id>/", views.product_detail),
    path("collections/", views.colloection_list),
    path("collections/<int:pk>/", views.colloection_detail)
]
