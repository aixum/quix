# urls.py
from django.urls import path

from . import views

app_name = "algorithms"

urlpatterns = [
    # Main pages
    path("", views.algorithm_list, name="list"),
    path("<slug:slug>/", views.algorithm_detail, name="detail"),
    # HTMX endpoints for dynamic content
    path("<slug:slug>/step/<int:step_order>/", views.get_step, name="get_step"),
    path(
        "<slug:slug>/step/<int:step_order>/visualize/",
        views.visualize_step,
        name="visualize_step",
    ),
    # API for getting visualization data
    path(
        "api/<slug:slug>/step/<int:step_order>/data/",
        views.get_visualization_data,
        name="get_visualization_data",
    ),
    # Optional: Practice examples
    path("<slug:slug>/practice/", views.practice_list, name="practice_list"),
    path(
        "<slug:slug>/practice/<int:example_id>/",
        views.practice_detail,
        name="practice_detail",
    ),
]
