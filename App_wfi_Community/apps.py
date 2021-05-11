from django.apps import AppConfig


class AppWfiCommunityConfig(AppConfig):
    name = 'App_wfi_Community'

    def ready(self):
        from .signals import upvt_save_handler
