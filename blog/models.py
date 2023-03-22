from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
    name = models.TextField(_("Nombre"))

    def __str__(self):
        return self.name
class Comment(models.Model):
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
    name = models.TextField(_("Nombre"))
    post = models.ForeignKey("Post", verbose_name=_("Post"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

