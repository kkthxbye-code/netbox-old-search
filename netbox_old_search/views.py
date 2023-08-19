from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import View
from .forms import SearchForm
from .search import SEARCH_TYPES

SEARCH_MAX_RESULTS = 100


class SearchView(View):
    def get(self, request):
        form = SearchForm(request.GET)
        results = []

        if form.is_valid():
            # If an object type has been specified, redirect to the dedicated view for it
            if form.cleaned_data["obj_type"]:
                object_type = form.cleaned_data["obj_type"]
                url = reverse(SEARCH_TYPES[object_type]["url"])
                return redirect(f"{url}?q={form.cleaned_data['q']}")

            for obj_type in SEARCH_TYPES.keys():
                queryset = SEARCH_TYPES[obj_type]["queryset"].restrict(request.user, "view")
                filterset = SEARCH_TYPES[obj_type]["filterset"]
                table = SEARCH_TYPES[obj_type]["table"]
                url = SEARCH_TYPES[obj_type]["url"]

                # Construct the results table for this object type
                filtered_queryset = filterset({"q": form.cleaned_data["q"]}, queryset=queryset).qs
                table = table(filtered_queryset, orderable=False)
                table.paginate(per_page=SEARCH_MAX_RESULTS)

                if table.page:
                    results.append({"name": queryset.model._meta.verbose_name_plural, "table": table, "url": f"{reverse(url)}?q={form.cleaned_data.get('q')}"})

        return render(
            request,
            "netbox_old_search/search.html",
            {
                "form": form,
                "results": results,
            },
        )
