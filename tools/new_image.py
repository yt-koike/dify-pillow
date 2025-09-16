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


class NewImage(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        invoke tools
        """
        width, height = [int(tool_parameters.get(key)) for key in ["width", "height"]]
        img = Image.new("RGBA", (width, height), color=(255, 255, 255, 255))
        io_bytes = io.BytesIO()
        img.save(io_bytes, format="PNG")
        yield self.create_blob_message(
            blob=io_bytes.getvalue(),
            meta={"filename": "output.png", "mime_type": "image/png"},
        )
