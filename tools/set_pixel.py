from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import (
    ToolInvokeMessage,
)
from tools.common import DifyPillow


class SetPixel(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        invoke tools
        """
        x, y, r, g, b, alpha = [
            int(tool_parameters.get(key)) for key in ["x", "y", "r", "g", "b", "alpha"]
        ]
        file = tool_parameters.get("image")
        if file is None:
            raise Exception("Please input an image")
        pil = DifyPillow(file.blob)
        pil.set_pixel(x, y, r, g, b, alpha)
        yield self.create_blob_message(
            blob=pil.get_blob(),
            meta={"filename": "output.png", "mime_type": "image/png"},
        )
