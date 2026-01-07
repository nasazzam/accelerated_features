"""
XFeat: Accelerated Features for Lightweight Image Matching, CVPR 2024.
https://www.verlab.dcc.ufmg.br/descriptors/xfeat_cvpr24/

This package provides fast and accurate local feature detection and matching
for computer vision applications.
"""

__version__ = "1.0.0"
__author__ = "Guilherme Potje, Felipe Cadar, Andre Araujo, Renato Martins, Erickson R. Nascimento"

# Import main classes for easier access
try:
    from modules.xfeat import XFeat
    from modules.model import XFeatModel
    from modules.lighterglue import LighterGlue
    
    __all__ = ['XFeat', 'XFeatModel', 'LighterGlue']
except ImportError:
    # Handle case where dependencies might not be installed yet
    pass

