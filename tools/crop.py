from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import (
    ToolInvokeMessage,
)
from tools.common import DifyPillow


class Crop(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        invoke tools
        """
        left_x, top_y, right_x, bottom_y = [
            tool_parameters[key] for key in ["left_x", "top_y", "right_x", "bottom_y"]
        ]
        file = tool_parameters.get("image")
        if file is None:
            raise Exception("Please input an image")
        pil = DifyPillow(file.blob)
        pil.crop(left_x, top_y, right_x, bottom_y)
        yield self.create_blob_message(
            blob=pil.get_blob(),
            meta={"filename": "output.png", "mime_type": "image/png"},
        )
