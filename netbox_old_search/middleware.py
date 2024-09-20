from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

plugin_settings = settings.PLUGINS_CONFIG.get("netbox_old_search", {})


class SearchRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if plugin_settings.get("replace_search") and request.path.startswith("/search/"):
            redirect_url = reverse("plugins:netbox_old_search:customsearch")

            return redirect(f"{redirect_url}?{request.GET.urlencode()}")

        return response
