# invoke-swap-dimensions
These two simple nodes for InvokeAI let you easily swap the width and height values for images. The Aspect Preset allows you to select a preset aspect ratio.


##Swap Dimensions Node for InvokeAI
##Allows swapping width and height values with a toggle

---

Connect the Swap Dimensions node directly to the Denoise node. When the SWAP toggle is activated, the width and height values are swapped.

---

##Aspect Preset Node for InvokeAI

Connect the Aspect Preset Node directly to the Denoise Node. Select a preset.

---

##Recommended workflow:

Connect the Aspect Preset node to the Swap Dimension node. Then connect the Swap Dimension node directly to the Denoise node.
