from PIL import Image
import torch
import numpy as np

# Tensor to PIL
def tensor2pil(img):
    return Image.fromarray(np.clip(255. * img.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

# PIL to Tensor
def pil2tensor(img):
    return torch.from_numpy(np.array(img).astype(np.float32) / 255.0).unsqueeze(0)