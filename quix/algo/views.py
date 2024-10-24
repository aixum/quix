# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Algorithm
from .models import AlgorithmStep
from .models import PracticeExample


def algorithm_list(request):
    if request.GET.get("type") and request.headers.get("HX-Request"):
        algo_type = request.GET.get("type")
        algorithms = Algorithm.objects.filter(algorithm_type=algo_type)
        return render(
            request,
            "algorithms/partials/list.html",
            {"algorithms": algorithms},
        )

    search = request.GET.get("search") if request.GET.get("search") else ""
    algorithms = Algorithm.objects.filter(name__icontains=search)
    algorithms = algorithms.order_by("name")
    if request.headers.get("HX-Request"):
        return render(
            request,
            "algorithms/partials/list.html",
            {"algorithms": algorithms},
        )
    algorithm_types = Algorithm.AlgorithmType.choices
    return render(
        request,
        "algorithms/list.html",
        {"algorithms": algorithms, "algorithm_types": algorithm_types},
    )


def algorithm_detail(request, slug):
    algorithm = get_object_or_404(Algorithm, slug=slug)
    first_step = algorithm.algorithmstep_set.first()
    return render(
        request,
        "algorithms/detail.html",
        {"algorithm": algorithm, "current_step": first_step},
    )


def get_step(request, slug, step_order):
    algorithm = get_object_or_404(Algorithm, slug=slug)
    step = get_object_or_404(AlgorithmStep, algorithm=algorithm, order=step_order)
    return render(request, "algorithms/partials/step.html", {"step": step})


def visualize_step(request, slug, step_order):
    algorithm = get_object_or_404(Algorithm, slug=slug)
    step = get_object_or_404(AlgorithmStep, algorithm=algorithm, order=step_order)
    return render(request, "algorithms/partials/visualization.html", {"step": step})


def get_visualization_data(request, slug, step_order):
    """API endpoint for getting raw visualization data"""
    algorithm = get_object_or_404(Algorithm, slug=slug)
    step = get_object_or_404(AlgorithmStep, algorithm=algorithm, order=step_order)
    return JsonResponse(step.visualization_data)


def practice_list(request, slug):
    algorithm = get_object_or_404(Algorithm, slug=slug)
    examples = algorithm.practiceexample_set.all()
    return render(
        request,
        "algorithms/practice_list.html",
        {"algorithm": algorithm, "examples": examples},
    )


def practice_detail(request, slug, example_id):
    algorithm = get_object_or_404(Algorithm, slug=slug)
    example = get_object_or_404(PracticeExample, algorithm=algorithm, id=example_id)
    return render(
        request,
        "algorithms/practice_detail.html",
        {"algorithm": algorithm, "example": example},
    )
