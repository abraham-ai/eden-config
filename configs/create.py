from dataclasses import dataclass

from .base import BaseConfig


@dataclass
class CreationConfig(BaseConfig):
    
    # dimensions
    n_samples: int = 1

    # prompts
    uc_text: str = "poorly drawn face, ugly, tiling, out of frame, extra limbs, disfigured, deformed body, blurry, blurred, watermark, text, grainy, signature, cut off, draft"
    text_input: str = "the quick brown fox jumps over the lazy dog"

    # init image
    init_image_data: str = None
    init_image_strength: float = 0.0

    # mask
    mask_image_data: str = None
    mask_brightness_adjust: float = 1.0
    mask_contrast_adjust: float = 1.0
    mask_invert: bool = False

    # seed
    seed: int = 0
