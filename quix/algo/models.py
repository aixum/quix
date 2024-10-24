from django.db import models


class Algorithm(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    # Complexity analysis
    time_complexity = models.CharField(max_length=50)
    space_complexity = models.CharField(max_length=50)

    # Implementation
    python_code = models.TextField()

    class AlgorithmType(models.TextChoices):
        SORTING = "SORT", "Sorting"
        SEARCHING = "SEARCH", "Searching"
        GRAPH = "GRAPH", "Graph"
        DYNAMIC = "DP", "Dynamic Programming"

    algorithm_type = models.CharField(max_length=10, choices=AlgorithmType.choices)

    def __str__(self):
        return f"{self.name} ({self.get_algorithm_type_display()})"


class AlgorithmStep(models.Model):
    """
    Each algorithm is broken down into learning steps
    """

    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()

    # Each step can have its own visualization
    visualization_data = models.JSONField(null=True)

    class Meta:
        ordering = ["order"]
        unique_together = ["algorithm", "order"]

    def __str__(self):
        return f"Step {self.order}: {self.title} ({self.algorithm.name})"


class PracticeExample(models.Model):
    """
    Real-world examples and practice problems
    """

    algorithm = models.ForeignKey(Algorithm, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    problem_description = models.TextField()
    input_example = models.TextField()
    output_example = models.TextField()
    explanation = models.TextField()

    def __str__(self):
        return f"Example: {self.title} for {self.algorithm.name}"
