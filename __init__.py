"""
Image Sizes Custom Nodes for InvokeAI
Provides dimension swapping and aspect ratio presets
"""

# Import with explicit error handling for debugging
try:
    from .swap_dimensions import SwapDimensionsInvocation
except ImportError as e:
    print(f"Failed to import SwapDimensionsInvocation: {e}")
    SwapDimensionsInvocation = None

try:
    from .aspect_preset import AspectPresetInvocation
except ImportError as e:
    print(f"Failed to import AspectPresetInvocation: {e}")
    AspectPresetInvocation = None

# Only export successfully imported classes
__all__ = []
if SwapDimensionsInvocation is not None:
    __all__.append("SwapDimensionsInvocation")
if AspectPresetInvocation is not None:
    __all__.append("AspectPresetInvocation")