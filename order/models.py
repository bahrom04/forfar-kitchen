from django.db import models


# Create your models here.
class Printer(models.Model):
    title = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    check_type = models.CharField(
        max_length=255, choices=[("kitchen", "Kitchen"), ("client", "Client")]
    )
    point_id = models.IntegerField()

    def __str__(self):
        return self.title


class Check(models.Model):
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)

    type = models.CharField(
        max_length=10, choices=[("kitchen", "Kitchen"), ("client", "Client")]
    )
    order = models.JSONField()
    status = models.CharField(
        max_length=10,
        choices=[("new", "New"), ("rendered", "Rendered"), ("printed", "Printed")],
    )
    pdf_file = models.FileField(upload_to="pdf/")

    def __str__(self):
        return f"Check {self.id} - {self.type}"
