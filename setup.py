from setuptools import setup, find_packages

setup(
    name='ComfyUI_ControlnetAux',
    version='1.0.0',
    description='ComfyUI Custom Node: ControlNet Auxiliar',
    long_description='This ComfyUI custom node, named ControlNet Auxiliar, is designed to provide auxiliary functionalities for image processing tasks. It is particularly useful for various image manipulation and enhancement operations. The node is integrated with functionalities for converting images between different formats and applying various image processing techniques.',
    author='Cornea Valentin',
    author_email='valicornea84@gmail.com',
    url='https://github.com/madtunebk/ComfyUI-ControlnetAux',
    packages=find_packages(),
    install_requires=[
        'timm==0.6.12',
        'controlnet-aux==0.0.7',
    ],
)
