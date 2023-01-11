from dataclasses import dataclass
from dataclasses import field
from typing import List

from .base import AnimationConfig


@dataclass
class Real2RealConfig(AnimationConfig):

    # anchor init images
    interpolation_init_images: List = field(default_factory=lambda: [])
    interpolation_init_images_top_k: int = 2
    interpolation_init_images_power: float = 3.0
    interpolation_init_images_min_strength: float = 0.2
    interpolation_init_images_max_strength: float = 0.95

    # seeds 
    interpolation_seeds: List = field(default_factory=lambda: [])
