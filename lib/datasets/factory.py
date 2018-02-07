# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""Factory method for easily getting imdbs by name."""

__sets = {}

from datasets.srd import srd
import numpy as np

# folder name
name = 'srd_image'
# folder path
devkit = '/home/garylau/projects/SRD/data/'
__sets['srd'] = (lambda name = name,devkit = devkit: srd(name,devkit))

def get_imdb(name):
    """Get an imdb (image database) by name."""
    if not __sets.has_key(name):
        raise KeyError('Unknown dataset: {}'.format(name))
    return __sets[name]()

def list_imdbs():
    """List all registered imdbs."""
    return __sets.keys()
