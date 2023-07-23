from . import ui
from . import room_layout
from . import building_config
from . import install_uninstall


def register():
    ui._register()
    room_layout._register()
    building_config._register()
    install_uninstall._register()


def unregister():
    ui._unregister()
    room_layout._unregister()
    building_config._unregister()
    install_uninstall._unregister()
