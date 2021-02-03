from django.db import models
from django.conf import settings
from django.utils import timezone
#from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MaxValueValidator, MinValueValidator,
    RegexValidator
)

from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


class Videos(models.Model):
    """
    Guest Details
    """

    fb_id = models.CharField(
        _("FB Id"), max_length=50
    )
    description = models.CharField(
        _("Description"), max_length=320
    )
    video = models.CharField(
        _("Video"), max_length=500
    )
    thum = models.CharField(
        _("Thumbnail"), max_length=500
    )
    gif = models.CharField(
        _("GIF"), max_length=500
    )
    view = models.IntegerField(
        _("Views"), default=0
    )
    section = models.CharField(
        _("Section"), max_length=250,
        default='0'
    )
    sound_id = models.IntegerField(
        _("Sound ID"), default=0
    )
    privacy_type = models.CharField(
        _("Privacy Type"), max_length=155,
        default='public'
    )
    allow_comments = models.BooleanField(
        _("Allow Comments"), default=True
    )
    created = models.DateTimeField(
        _("Created"), auto_now_add=True,
        auto=now
    )
    latitude = models.DecimalField(
        _("Latitude"), max_digits=17, decimal_places=13,
        default=0
    )
    longitude = models.DecimalField(
        _("Longitude"), max_digits=17, decimal_places=13,
        default=0
    )
    video_transcript = models.CharField(
        _("Transcript"), max_length=512
    )
    title = models.CharField(
        _("Title"), max_length=100
    )

    def __str__(self):
        return "%s" % (self.title)

    class Meta:
        ordering = ["-created"]


class VideoLikeDisLike(models.Model):
    """
    Video Like & Dislike
    """

    fb_id = models.CharField(
        _("FB Id"), max_length=50
    )
    video_id = models.ForeignKey(
        _("Video ID"), max_length=50
    )
    action = models.IntegerField(
        _("Action"), default=0
    )
    created = models.DateTimeField(
        _("Created"), auto_now_add=True,
        auto=now
    )
    
    def __str__(self):
        return "%s" % (self.video_id)

    class Meta:
        ordering = ["-created"]


class VideoWatchAudit(models.Model):
    """
    Video Watch Audit
    """

    fb_id = models.CharField(
        _("FB Id"), max_length=50
    )
    video_id = models.ForeignKey(
        _("Video ID"), max_length=50
    )
    created = models.DateTimeField(
        _("Created"), auto_now_add=True,
        auto=now
    )
    
    def __str__(self):
        return "%s" % (self.video_id)

    class Meta:
        ordering = ["-created"]