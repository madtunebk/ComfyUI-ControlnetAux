"""
@author: Cornea Valentin
@title: ComfyUI ControlnetAux
@nickname: ComfyUI ControlnetAux
@description: This ComfyUI custom node, named ControlNet Auxiliar, is designed to provide auxiliary functionalities for image processing tasks. It is particularly useful for various image manipulation and enhancement operations. The node is integrated with functionalities for converting images between different formats and applying various image processing techniques.
"""
import sys 
import os

version_code = [0, 3]
version_str  = f"V{version_code[0]}.{version_code[1]}" + (f'.{version_code[2]}' if len(version_code) > 2 else ' beta')
print(f"### Loading: ControlnetAux ({version_str})")


sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "comfy"))

from .nodes.nodes import NODE_CLASS_MAPPINGS as controlnetaux_NODE_CLASS_MAPPINGS,  NODE_DISPLAY_NAME_MAPPINGS as controlnetaux_NODE_DISPLAY_NAME_MAPPINGS

NODE_CLASS_MAPPINGS = {
    **controlnetaux_NODE_CLASS_MAPPINGS,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **controlnetaux_NODE_DISPLAY_NAME_MAPPINGS,
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']