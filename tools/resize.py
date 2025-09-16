from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import (
    ToolInvokeMessage,
)
from tools.common import DifyPillow


class Resize(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        invoke tools
        """
        width, height = [int(tool_parameters.get(key)) for key in ["width", "height"]]
        file = tool_parameters.get("image")
        if file is None:
            raise Exception("Please input an image")
        pil = DifyPillow(file.blob)
        pil.resize(width, height)
        yield self.create_blob_message(
            blob=pil.get_blob(),
            meta={"filename": "output.png", "mime_type": "image/png"},
        )
