from extras.plugins import PluginConfig
from .middleware import SearchRedirectMiddleware


class NetboxOldSearch(PluginConfig):
    name = "netbox_old_search"
    verbose_name = "Old Search"
    description = "Netbox Old Search"
    version = "0.1"
    base_url = "old-search"
    default_settings = {"show_menu": False, "replace_search": True}
    middleware = ["netbox_old_search.middleware.SearchRedirectMiddleware"]


config = NetboxOldSearch
