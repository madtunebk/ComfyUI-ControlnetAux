"""
@author: Cornea Valentin
@title: ComfyUI ControlnetAux
@nickname: ComfyUI ControlnetAux
@description: This ComfyUI custom node, named ControlNet Auxiliar, is designed to provide auxiliary functionalities for image processing tasks. It is particularly useful for various image manipulation and enhancement operations. The node is integrated with functionalities for converting images between different formats and applying various image processing techniques.
"""

from .nodes import controlnet_auxiar

version_code = [0, 67]
version_str = f"V{version_code[0]}.{version_code[1]}" + (f'.{version_code[2]}' if len(version_code) > 2 else '')
print(f"### Loading: ControlnetAux ({version_str})")

node_list = [
    "controlnetaux",
]