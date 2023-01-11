from dataclasses import dataclass


@dataclass
class BaseConfig:

    # dimensions
    width: int = 512
    height: int = 512
    upscale_f: float = 1.0    

    # sampling params
    sampler: str = "klms"
    steps: int = 50
    scale: float = 10.0

    # streaming back results
    stream: bool = False
    stream_every: int = 1
