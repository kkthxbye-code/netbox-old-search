from django.shortcuts import redirect
from django.urls import reverse


class SearchRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.path.startswith("/search/") and request.GET:
            redirect_url = reverse("plugins:netbox_old_search:customsearch")

            return redirect(f"{redirect_url}?{request.GET.urlencode()}")

        return response
