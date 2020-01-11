from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=200, unique=True, db_index=True)
    image = models.ImageField(
        upload_to="images/", height_field="height", width_field="width"
    )

    height = models.IntegerField(blank=True, editable=False)
    width = models.IntegerField(blank=True, editable=False)

    def __str__(self):
        return self.name
