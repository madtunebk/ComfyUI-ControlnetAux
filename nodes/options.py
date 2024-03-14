from collections import namedtuple

# Define a named tuple for parameter information
ParameterInfo = namedtuple("ParameterInfo", ["type", "default", "min", "max", "step"])

# Define the optional parameters using the named tuple
optional_params = {
    "hed": {
        "safe": ParameterInfo("BOOLEAN", False, False, True, None),
        "scribble": ParameterInfo("BOOLEAN", False, False, True, None)
    },
    "openpose": {
        "include_body": ParameterInfo("BOOLEAN", True, False, True, None),
        "include_hand": ParameterInfo("BOOLEAN", True, False, True, None),
        "include_face": ParameterInfo("BOOLEAN", True, False, True, None)
    },
    "mlsd": {
        "thr_v": ParameterInfo("FLOAT", 0.1, 0.01, 1.0, 0.01),
        "thr_d": ParameterInfo("FLOAT", 0.1, 0.01, 1.0, 0.01)
    },
    "pidi": {
        "safe": ParameterInfo("BOOLEAN", True, False, True, None),
        "scribble": ParameterInfo("BOOLEAN", True, False, True, None),
        "apply_filter": ParameterInfo("BOOLEAN", True, False, True, None),
    },
    "lineart": {
        "coarse": ParameterInfo("BOOLEAN", False, False, True, None),
    },
    "depth_leres": {
        "boost": ParameterInfo("BOOLEAN", False, False, True, None),
    },
    "content": {
        "h": ParameterInfo("INT", 512, 1, 1024, 1),
        "w": ParameterInfo("INT", 512, 1, 1024, 1),
        "f": ParameterInfo("INT", 10, 1, 1024, 1),
    },
    "face_detector": {
        "max_faces": ParameterInfo("INT", 1, 1, 5, 1),
        "min_confidence": ParameterInfo("FLOAT", 0.5, 0.01, 1.0, 0.01),
    },
    "canny": {
        "low_threshold": ParameterInfo("INT", 100, 1, 200, 1),
        "high_threshold": ParameterInfo("INT", 200, 1, 200, 1),
    }
}
