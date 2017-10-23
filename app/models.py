from django.db.models import Model, FileField


class File(Model):
    file = FileField(upload_to='media/', blank=True, null=True)
