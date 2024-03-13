"""
@author: Cornea Valentin
@title: ComfyUI ControlnetAux
@nickname: ComfyUI ControlnetAux
@description: This ComfyUI custom node, named ControlNet Auxiliar, is designed to provide auxiliary functionalities for image processing tasks. It is particularly useful for various image manipulation and enhancement operations. The node is integrated with functionalities for converting images between different formats and applying various image processing techniques.
"""

from controlnet_aux.processor import Processor
import traceback

from .funcs import pil2tensor, tensor2pil


class controlnet_auxiar:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):  # Changed s to cls
        modules  = [ "scribble_hed", "softedge_hed", "scribble_hedsafe", "softedge_hedsafe", "depth_midas", "openpose", "openpose_face", "openpose_faceonly", "openpose_full", "openpose_hand", "scribble_pidinet", "softedge_pidinet", "scribble_pidsafe", "softedge_pidsafe", "normal_bae", "lineart_coarse", "lineart_realistic", "lineart_anime", "depth_zoe", "depth_leres", "depth_leres++", "shuffle", "mediapipe_face", "canny"]
        return {
            "required": {
                "image": ("IMAGE",),
                "mode": ([modules, ])
            },
            "optional": {
                "low_threshold": ("INT", {"default": 50, "min": 1, "max": 200, "step": 1}),
                "high_threshold": ("INT", {"default": 100, "min": 1, "max": 200, "step": 1}),
                "image_resolution": ("INT", {"default": 512, "min": 512, "max": 1024, "step": 1}),
            }
        }
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "process_image"
    CATEGORY = "image"

    def process_image(self, image, mode, low_threshold,  high_threshold, image_resolution):
        convert_image = tensor2pil(image)
        try:
            if mode == "canny":
                params = {"low_threshold": low_threshold, "high_threshold" : high_threshold, "image_resolution": image_resolution}
            else: 
                params = {}
            
            processor = Processor(mode, params=params)
            processed_image = processor(convert_image, to_pil=True)
            return (pil2tensor(processed_image),)
        except:
            print(type(convert_image))
            traceback.print_exc()
            raise ValueError("Unsupported image format")

NODE_CLASS_MAPPINGS = {
    "ControlNet Auxiliar": controlnet_auxiar
}
