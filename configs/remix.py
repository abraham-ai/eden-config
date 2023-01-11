from dataclasses import dataclass

from .base import BaseConfig


@dataclass
class RemixConfig(BaseConfig):

    # dimensions
    n_samples: int = 1

    # uc_text
    uc_text: str = "poorly drawn face, ugly, tiling, out of frame, extra limbs, disfigured, deformed body, blurry, blurred, watermark, text, grainy, signature, cut off, draft"

    # init image
    init_image_data: str = None
    init_image_strength: float = 0.0

    # seed
    seed: int = 0
