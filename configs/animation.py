from dataclasses import dataclass

from .base import BaseConfig


@dataclass
class AnimationConfig(BaseConfig):

    # animation settings
    n_frames: int = 10
    loop: bool = False
    smooth: bool = False  
    n_film: int = 0
    scale_modulation: float = 0.0
    latent_smoothing_std: float = 0.01

    # video settings
    fps: int = 12
        