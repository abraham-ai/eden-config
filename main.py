from configs.create import CreateConfig

config = CreateConfig(
    text_input = "The World is a Vampire",
)

print(config)


from dataclasses import dataclass
from dataclasses import field
from typing import List


@dataclass
class DefaultFields:
    
    # config and checkpoint
    config: str = 'sd_yaml'
    ckpt: str = 'sd_ckpt'
    precision: str = 'autocast'
    half_precision: bool = True
    
    # unused/defaulted
    activate_tileable_textures: bool = False
    ddim_eta: float = 0.0
    C: int = 4
    f: int = 8   
    dynamic_threshold: float = None
    static_threshold: float = None
    init_image_inpaint_mode: str = None # ["mean_fill", "edge_pad", "cv2_telea", "cv2_ns"]
    clip_interrogator_mode: str = 'full' # ["full", "fast"]

    #init_sample: str = None
    #init_latent: str = None
    #init_image: Image = None
    #mask_image: Image = None

    # aesthetic gradients
    aesthetic_target: List = None    # either a path to a .pt file, or a list of PIL.Image objects
    aesthetic_steps: int = 0
    aesthetic_lr: float = 0.0001
    ag_L2_normalization_constant: float = 0.05

