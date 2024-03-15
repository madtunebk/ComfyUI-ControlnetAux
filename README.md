# ComfyUI Custom Node: ControlNet Auxiliar

This ComfyUI custom node, ControlNet Auxiliar, provides auxiliary functionalities for image processing tasks. It supports various image manipulation and enhancement operations.

### Python Package Requirements

- **timm==0.6.12**
- **controlnet-aux==0.0.7**
- **mediapipe**

# Manual Installation Guide for ComfyUI-ControlnetAux

1. **Clone the Repository:**
   - Open your terminal.
   - Navigate to the directory where ComfyUI is installed, ensure that you are in the `custom_nodes` folder (e.g., `ComfyUI/custom_nodes/` ).
   - Run the following command:
     ```bash
     git clone https://github.com/madtunebk/ComfyUI-ControlnetAux.git
     ```

2. **Install Dependencies:**
   - Navigate into the cloned directory:
     ```bash
     cd ComfyUI-ControlnetAux
     ```
   - Activate the virtual environment:
     ```bash
     source ../../venv/bin/activate
     ```
   - Install the required Python packages using pip:
     ```bash
     pip install -r requirements.txt
     ```
   - To support **DWPose** which is dependent on **MMDetection**, **MMCV**, and **MMPose**, you need to install additional packages:
     ```bash
     pip install openmim
     mim install mmengine
     mim install "mmcv>=2.0.1"
     mim install "mmdet>=3.1.0"
     mim install "mmpose>=1.1.0"
     ```

3. **Run the Application:**
   - Once the dependencies are installed, you can run the application.

This installation guide is for Ubuntu Linux.


## Usage

### Input Types

- **image**: Input image for processing.
- **mode**: Processing mode, including options like scribble_hed, softedge_hed, depth_midas, openpose, etc.

### Return Types

The node returns processed images.

### Functionality

- **process_image**: Processes input image based on specified mode and parameters.


## Example Workflow
![Example Workflow](/workflows/example.png) [Download Example Workflow JSON](/workflows/example.json)

## Note: Work in Progress

This project is under development. Contributions and feedback are welcome!

## Node Class Mappings

The ControlNet Auxiliar node is mapped to various classes corresponding to different models:

- `controlaux_hed`: HED model for edge detection.
- `controlaux_midas`: Midas model for depth estimation.
- `controlaux_mlsd`: MLSD model for line segment detection.
- `controlaux_openpose`: Openpose model for human pose estimation.
- `controlaux_dwpose`: DWPose model for human pose estimation.
- `controlaux_pidi`: PidiNet model for image inpainting.
- `controlaux_normal_bae`: NormalBae model for image restoration.
- `controlaux_lineart`: Lineart model for image stylization.
- `controlaux_lineart_anime`: Lineart Anime model for anime-style image stylization.
- `controlaux_zoe`: Zoe model for depth super-resolution.
- `controlaux_sam`: SAM model for image segmentation.
- `controlaux_leres`: Leres model for image restoration.
- `controlaux_canny`: Canny model for edge detection.
- `controlaux_content`: Content Shuffle model for image processing.
- `controlaux_face_detector`: Mediapipe Face Detector for face detection.

---

**Credit**: Developed using source from [lllyasviel](https://github.com/lllyasviel).
