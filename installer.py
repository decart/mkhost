import pkg_resources
import sys

from pyimod03_importers import FrozenImporter

from mkhost import main

# Fix for pyinstaller
if getattr(sys, 'frozen', False):
   pkg_resources.register_loader_type(
       FrozenImporter, pkg_resources.DefaultProvider
   )

main()