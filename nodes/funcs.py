from PIL import Image
import torch
import numpy as np


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Tensor to PIL
def tensor2pil(tensor):
    """
    Converts a torch tensor or a batch of tensors to PIL images.
    
    Args:
        tensor (torch.Tensor): Input tensor or batch of tensors.
        
    Returns:
        List[Image.Image] or Image.Image: Converted PIL images or a single PIL image.
    """
    if tensor.ndimension() == 4:  # Check if the input is a batch of images
        return [Image.fromarray(np.clip(255.0 * t.cpu().numpy().squeeze(), 0, 255).astype(np.uint8)) for t in tensor]
    return Image.fromarray(np.clip(255.0 * tensor.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

# PIL to Tensor
def pil2tensor(images):
    """
    Converts PIL images or a list of PIL images to a torch tensor.
    
    Args:
        images (Image.Image or List[Image.Image]): Input PIL image or list of images.
        
    Returns:
        torch.Tensor: Converted tensor.
    """
    if isinstance(images, list):  # Check if the input is a list of images
        tensors = [torch.from_numpy(np.array(img).astype(np.float32) / 255.0).unsqueeze(0).to(device) for img in images]
        return torch.cat(tensors, dim=0)
    return torch.from_numpy(np.array(images).astype(np.float32) / 255.0).unsqueeze(0).to(device)
