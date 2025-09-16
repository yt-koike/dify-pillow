from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import (
    ToolInvokeMessage,
)
from tools.common import DifyPillow


class SimpleOPs(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        """
        invoke tools
        """
        feature = tool_parameters.get("feature")
        file = tool_parameters.get("image")
        if file is None:
            raise Exception("Please input an image")
        pil = DifyPillow(file.blob)
        if feature == "vflip":
            pil.vflip()
        elif feature == "hflip":
            pil.hflip()
        elif feature == "2jpeg":
            yield self.create_blob_message(
                blob=pil.get_blob("JPEG"),
                meta={"filename": "output.jpg", "mime_type": "image/jpeg"},
            )
            return
        elif feature == "2bmp":
            yield self.create_blob_message(
                blob=pil.get_blob("BMP"),
                meta={"filename": "output.bmp", "mime_type": "image/bmp"},
            )
            return
        elif feature == "2webp":
            yield self.create_blob_message(
                blob=pil.get_blob("WEBP"),
                meta={"filename": "output.webp", "mime_type": "image/webp"},
            )
            return
        yield self.create_blob_message(
            blob=pil.get_blob(),
            meta={"filename": "output.png", "mime_type": "image/png"},
        )
