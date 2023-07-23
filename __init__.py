from .src import register, unregister
bl_info = {
    "name": "Victorian Asset Library Installer",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "description": "Adds a button to install Victorian Asset Library",
    "category": "Assets",
}


def unregister():
    unregister()


if __name__ == "__main__":
    register()
