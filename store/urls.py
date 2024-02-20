from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path("products/", views.ProductList.as_view()),
    path("products/<int:pk>/", views.ProductDetail.as_view()),
    path("collections/", views.colloection_list),
    path("collections/<int:pk>/", views.colloection_detail)
]
