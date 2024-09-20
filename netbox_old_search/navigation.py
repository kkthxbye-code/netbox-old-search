from django.conf import settings
from netbox.plugins import PluginMenuItem

plugin_settings = settings.PLUGINS_CONFIG.get("netbox_old_search", {})

if plugin_settings.get("show_menu"):
    menu_items = (
        PluginMenuItem(
            link="plugins:netbox_old_search:customsearch",
            link_text="Old Search",
        ),
    )
