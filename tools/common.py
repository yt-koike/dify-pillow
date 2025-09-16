from enum import StrEnum
import io
from PIL import Image, ImageDraw


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


class DifyPillow:
    def __init__(self, blob: bytes | None = None):
        if blob is None:
            self.img = Image.new("RGBA", (256, 256), color=(255, 255, 255, 255))
        else:
            self.img = Image.open(io.BytesIO(blob)).convert("RGBA")

    def resize(self, width: int, height: int):
        self.img = self.img.resize((width, height))

    def rotate(self, angle):
        self.img = self.img.rotate(angle)

    def crop(
        self,
        left_x: int,
        top_y: int,
        right_x: int,
        bottom_y: int,
    ):
        self.img = self.img.crop((left_x, top_y, right_x, bottom_y))

    def fill_rect(
        self,
        left_x: int,
        top_y: int,
        right_x: int,
        bottom_y: int,
        fill: tuple[int] | None = (255, 255, 255, 255),
        outline: tuple[int] | None = None,
        width: int = 10,
    ):
        d = ImageDraw.Draw(self.img)
        d.rectangle(
            [(left_x, top_y), (right_x, bottom_y)],
            fill=fill,
            outline=outline,
            width=width,
        )

    def fill(self, fill: tuple[int] | None = (255, 255, 255, 255)):
        self.fill_rect(0, 0, self.img.width - 1, self.img.height - 1, fill)

    def hflip(self):
        self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)

    def vflip(self):
        self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)

    def get_pixel(self, x, y) -> tuple:
        return self.img.getpixel((x, y))

    def set_pixel(self, x, y, r, g, b, alpha) -> tuple:
        return self.img.setpixel((x, y), (r, g, b, alpha))

    def get_blob(self, format="PNG") -> bytes:
        io_bytes = io.BytesIO()
        if format in ["BMP", "JPEG"]:
            self.img = self.img.convert("RGB")
        self.img.save(io_bytes, format=format)
        return io_bytes.getvalue()
