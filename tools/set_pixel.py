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


class SetPixel(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        invoke tools
        """
        x, y, r, g, b, alpha = [
            int(tool_parameters.get(key)) for key in ["x", "y", "r", "g", "b", "alpha"]
        ]
        file = tool_parameters.get("image")
        pil_img = Image.open(io.BytesIO(file.blob)).convert("RGBA")
        pil_img.putpixel((x, y), (r, g, b, alpha))
        io_bytes = io.BytesIO()
        pil_img.save(io_bytes, format="PNG")
        yield self.create_blob_message(
            blob=io_bytes.getvalue(),
            meta={"filename": "output.png", "mime_type": "image/png"},
        )
