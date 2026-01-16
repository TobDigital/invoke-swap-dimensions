"""
Swap Dimensions Node for InvokeAI
Allows swapping width and height values with a toggle
"""

from invokeai.invocation_api import (
    BaseInvocation,
    BaseInvocationOutput,
    invocation,
    invocation_output,
    InputField,
    OutputField,
)


@invocation_output("swap_dimensions_output")
class SwapDimensionsOutput(BaseInvocationOutput):
    """Output for Swap Dimensions"""
    
    width: int = OutputField(description="Width value")
    height: int = OutputField(description="Height value")


@invocation(
    "swap_dimensions",
    title="Swap Dimensions",
    tags=["image", "dimensions", "swap"],
    category="image_sizes",
    version="1.0.0",
)
class SwapDimensionsInvocation(BaseInvocation):
    """Swaps width and height dimensions based on toggle"""
    
    width: int = InputField(
        default=1024,
        ge=64,
        le=4096,
        description="Width in pixels"
    )
    
    height: int = InputField(
        default=1024,
        ge=64,
        le=4096,
        description="Height in pixels"
    )
    
    swap: bool = InputField(
        default=False,
        description="Toggle to swap width and height"
    )
    
    def invoke(self, context) -> SwapDimensionsOutput:
        """Swap dimensions if toggle is enabled"""
        
        if self.swap:
            output_width = self.height
            output_height = self.width
        else:
            output_width = self.width
            output_height = self.height
        
        return SwapDimensionsOutput(
            width=output_width,
            height=output_height
        )