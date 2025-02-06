## Inversion
from .nodes.model_pred_node import OutSD3ModelSamplingPredNode
## FlowEdit
from .nodes.flowedit_nodes import FlowEditSamplerNode, FlowEditCFGGuiderNode


NODE_CLASS_MAPPINGS = {
    ## Inversion
    "OutSD3ModelSamplingPred": OutSD3ModelSamplingPredNode,
    ## Flow-Edit
    "FlowEditSampler": FlowEditSamplerNode,
    "FlowEditCFGGuider": FlowEditCFGGuiderNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    ## Inversion
    "OutSD3ModelSamplingPred": "Outverse SD3 Model Pred",
    ## FlowEdit
    "FlowEditSampler": "Flow Edit Sampler",
    "FlowEditCFGGuider": "Flow Edit CFG Guider",
}

