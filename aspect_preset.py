"""Aspect Preset Node for InvokeAI"""

from typing import Literal
from invokeai.invocation_api import (
    BaseInvocation,
    BaseInvocationOutput,
    invocation,
    invocation_output,
    InputField,
    OutputField,
)


@invocation_output("aspect_preset_output")
class AspectPresetOutput(BaseInvocationOutput):
    """Output for Aspect Preset"""
    width: int = OutputField(description="Width value")
    height: int = OutputField(description="Height value")


@invocation(
    "aspect_preset",
    title="Aspect Preset",
    tags=["image", "dimensions", "aspect", "preset"],
    category="image_sizes",
    version="1.0.0",
)
class AspectPresetInvocation(BaseInvocation):
    """Provides preset aspect ratios for image generation"""
    
    preset: Literal[
        "1:1 Square",
        "4:5 Portrait",
        "2:3 Portrait",
        "9:16 Vertical",
        "16:9 Landscape",
        "3:2 Landscape",
        "21:9 Cinematic"
    ] = InputField(
        default="1:1 Square",
        description="Select aspect ratio preset"
    )
    
    def invoke(self, context) -> AspectPresetOutput:
        """Return dimensions for selected preset"""
        
        # Mapping of presets to dimensions (width, height)
        dimensions_map = {
            "1:1 Square": (1024, 1024),
            "4:5 Portrait": (896, 1120),
            "2:3 Portrait": (832, 1248),
            "9:16 Vertical": (768, 1360),
            "16:9 Landscape": (1360, 768),
            "3:2 Landscape": (1248, 832),
            "21:9 Cinematic": (1536, 656),
        }
        
        width, height = dimensions_map.get(self.preset, (1024, 1024))
        
        return AspectPresetOutput(width=width, height=height)