import os, glob, json

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate DataBase'

    def post_video_watch_audit(self):
        return True

    def post_video_like_dislike(self):
        return True

    def post_videos(self):
        return True

    def handle(self, *args, **kwargs):
        self.stdout.write("Initially Populated!")