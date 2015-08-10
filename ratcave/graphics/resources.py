__author__ = 'ratcave'

from os import path as __path

# This is an easy way to get the filepaths of some oft-used resources for displaying simple scenes.

resource_path = __path.join(__path.split(__file__)[0],'assets')

# Images
img_uvgrid = __path.join(resource_path,'uvgrid.png')
img_colorgrid = __path.join(resource_path, 'colorgrid.png')

# Meshes
obj_primitives = __path.join(resource_path, 'primitives.obj')