# ComfyUI Custom Node: ControlNet Auxiliar

This ComfyUI custom node, ControlNet Auxiliar, provides auxiliary functionalities for image processing tasks. It supports various image manipulation and enhancement operations.

## Manual Installation Guide

1. **Clone the Repository:**
   - Navigate to the `custom_nodes` directory in your ComfyUI installation.
   - Clone the repository:
     ```bash
     git clone https://github.com/madtunebk/ComfyUI-ControlnetAux.git
     ```

2. **Install Dependencies:**
   - Navigate to the cloned directory:
     ```bash
     cd ComfyUI-ControlnetAux
     ```
   - Activate the virtual environment:
     ```bash
     source ../../venv/bin/activate
     ```
   - Install required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Application:**
   - Follow instructions in the repository's README or documentation to use the application.

This guide is for Ubuntu Linux.

## Usage

### Input Types

- **image**: Input image for processing.
- **mode**: Processing mode, including options like scribble_hed, softedge_hed, depth_midas, openpose, etc.

### Return Types

The node returns processed images.

### Functionality

- **process_image**: Processes input image based on specified mode and parameters.

### Python Package Requirements

- **timm==0.6.12**
- **controlnet-aux==0.0.7**
- **mediapipe**

## Example Workflow
![Example Workflow](/workflows/example.png) [Download Example Workflow JSON](/workflows/example.json)

## Note: Work in Progress

This project is under development. Contributions and feedback are welcome!

## Node Class Mappings

The ControlNet Auxiliar node is mapped to the class `controlnet_auxiliary` in the `controlnet_aux.processor` module.

---

**Credit**: Developed using source from [lllyasviel](https://github.com/lllyasviel).
