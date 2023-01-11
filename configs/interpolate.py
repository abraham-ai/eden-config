from dataclasses import dataclass
from dataclasses import field
from typing import List

from .base import AnimationConfig


@dataclass
class InterpolateConfig(AnimationConfig):

    # anchor prompts
    interpolation_texts: List = field(default_factory=lambda: [])

    # seeds
    interpolation_seeds: List = field(default_factory=lambda: [])
