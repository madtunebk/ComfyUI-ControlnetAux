import traceback, os
from controlnet_aux import (
    HEDdetector, MidasDetector, MLSDdetector, OpenposeDetector,
    PidiNetDetector, NormalBaeDetector, LineartDetector,
    LineartAnimeDetector, CannyDetector, ContentShuffleDetector,
    ZoeDetector, MediapipeFaceDetector, SamDetector, LeresDetector, DWposeDetector
)
from .funcs import pil2tensor, tensor2pil, device
from .options import optional_params

# List of controlnet aux models that can be used
models = ['hed', 'midas', 'mlsd', 'openpose', "pidi", "dwpose", 'normal_bae', 'lineart',
          'lineart_anime', 'zoe', 'sam', 'leres', 'canny', 'content', 'face_detector']

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

def process_image_wrapper(self, image, modaux, **kwargs):
    try:
        tensor_pil = tensor2pil(image)
        detector = None
        if modaux == "hed":
            detector = HEDdetector.from_pretrained("lllyasviel/Annotators")
        elif modaux == "midas":
            detector = MidasDetector.from_pretrained("lllyasviel/Annotators")
        elif modaux == "mlsd":
            detector = MLSDdetector.from_pretrained("lllyasviel/Annotators")
        elif modaux == "openpose":
            detector = OpenposeDetector.from_pretrained("lllyasviel/Annotators")
        elif modaux == "dwpose":
            script_dir = os.path.dirname(os.path.abspath(__file__))
            det_config = os.path.join(script_dir, "dwpose/yolox_config/yolox_l_8xb8-300e_coco.py")
            pose_config = os.path.join(script_dir, "dwpose/dwpose_config/dwpose-l_384x288.py")
            detector = DWposeDetector(det_config=det_config, pose_config=pose_config, device=device) ## will need to fix it !!!
        elif modaux == "pidi":
            detector = PidiNetDetector.from_pretrained("lllyasviel/Annotators")
        elif modaux == "normal_bae":
            detector = NormalBaeDetector.from_pretrained("lllyasviel/Annotators")
        elif modaux == "lineart":
            detector = LineartDetector.from_pretrained("lllyasviel/Annotators")
        elif modaux == "lineart_anime":
            detector = LineartAnimeDetector.from_pretrained("lllyasviel/Annotators")
        elif modaux == "zoe":
            detector = ZoeDetector.from_pretrained("lllyasviel/Annotators")
        elif modaux == "sam":
            detector = SamDetector.from_pretrained("ybelkada/segment-anything", subfolder="checkpoints")
        elif modaux == "leres":
            detector = LeresDetector.from_pretrained("lllyasviel/Annotators")
        elif modaux == "canny":
            detector = CannyDetector()
        elif modaux == "content":
            detector = ContentShuffleDetector()
        elif modaux == "face_detector":
            detector = MediapipeFaceDetector()
        else:
            raise ValueError(f"Invalid modaux argument: {modaux}")
        processed_image = detector(tensor_pil, **kwargs)
        return (pil2tensor(processed_image),)
    except Exception as e:
        traceback.print_exc()
        raise ValueError(f"Error processing image: {e}")

for model_name in models:
    new_class = type(f"controlaux_{model_name}", (object,), {
        "__init__": lambda self: None,
        "INPUT_TYPES": classmethod(lambda cls, model_name=model_name: {
            "required": {"image": ("IMAGE",)},
            "modaux": model_name,
            "optional": optional_params.get(model_name, {})
        }),
        "RETURN_TYPES": ("IMAGE",),
        "FUNCTION": "process_image",
        "CATEGORY": "ControlNet Auxiliar",
        "process_image": lambda self, image, modaux=model_name, **kwargs: self._process_image(image, modaux, **kwargs)
    })
    
    setattr(new_class, "_process_image", process_image_wrapper)
    globals()[f"controlaux_{model_name}"] = new_class
    NODE_CLASS_MAPPINGS[f"controlaux_{model_name}"] = new_class
    NODE_DISPLAY_NAME_MAPPINGS[f"controlaux_{model_name}"] = f"modaux: {model_name}"
