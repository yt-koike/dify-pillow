from enum import StrEnum
import io
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import (
    ToolInvokeMessage,
)
from PIL import Image


class FileType(StrEnum):
    IMAGE = "image"
    DOCUMENT = "document"
    AUDIO = "audio"
    VIDEO = "video"
    CUSTOM = "custom"

    @staticmethod
    def value_of(value):
        for member in FileType:
            if member.value == value:
                return member
        raise ValueError(f"No matching enum found for value '{value}'")


class GetPixel(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        invoke tools
        """
        x, y = tool_parameters.get("x"), tool_parameters.get("y")
        file = tool_parameters.get("image")
        r, g, b, alpha = 0, 0, 0, 0
        if file.type == FileType.IMAGE:
            pil_img = Image.open(io.BytesIO(file.blob)).convert("RGBA")
            r, g, b, alpha = pil_img.getpixel((x, y))
        yield self.create_variable_message("r", r)
        yield self.create_variable_message("g", g)
        yield self.create_variable_message("b", b)
        yield self.create_variable_message("alpha", alpha)
