from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import (
    ToolInvokeMessage,
)
from tools.common import DifyPillow


class GetPixel(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        invoke tools
        """
        x, y = tool_parameters.get("x"), tool_parameters.get("y")
        file = tool_parameters.get("image")
        if file is None:
            raise Exception("Please input an image")
        pil = DifyPillow(file.blob)
        r, g, b, alpha = pil.getpixel((x, y))
        yield self.create_variable_message("r", r)
        yield self.create_variable_message("g", g)
        yield self.create_variable_message("b", b)
        yield self.create_variable_message("alpha", alpha)
