from django.db import models


class Teams(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.teammate}"


class People(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, default=None, null=True)
    team = models.ForeignKey(
        Teams,
        on_delete=models.CASCADE,
        related_name="teammate",
        null=True,
        default=None,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"
