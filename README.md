## dify-pillow

**Author:** yt-koike
**Version:** 0.0.1
**Type:** tool

### Description

dify-pillow is a standalone plugin for dify to enable image editing with a help of a Python library called [Pillow](https://pillow.readthedocs.io/en/stable/index.html).

### How to Use

Before using dify-pillow, you need to install it to your dify via [Dify Marketplace](https://marketplace.dify.ai/) or [GitHub](https://github.com/yt-koike/dify-pillow/releases).

After installation, the following nodes will be available. Note that most nodes output PNG files as the format supports alpha channel.

## Image Info

Image Info node reads a list of files and extract graphical information from each of them.
If the file is an image file, it will extract its resolution, color mode and MIME types.
If not, it will return its resolution as width=0 and height=0.

## Get Pixel

Get Pixel node returns a pixel on a given image.

## Set Pixel

Set Pixel node sets a pixel on a given image.

## New Image

New Image node creates a new white blank image.

## Resize

Resize node changes a given image's resolution.

## Crop

Crop node extracts a specified region from a given image.

## Rotate

Rotate node rotates the given image around its center.

## Simple OPs

Simple OPs node performs simple image edit operations which don't need any parameters.
It can flip an image vertically or horizontally, or convert it to another format including .jpeg, .bmp and .webp.

### Required APIs and Credentials

None. Cron is a standalone plugin.

### Connection requirements

None. Cron is a standalone plugin.

### Third-party LICENSE and Sources

Like PIL, Pillow and is [licensed under the open source MIT-CMU License](./LICENSE)

Pillow Logo(pillow-logo-400x400.png) created by Alastair Houghton: https://github.com/python-pillow/pillow-logo/tree/main

### External Links

- dify-pillow Repository: https://github.com/yt-koike/dify-pillow
- Pillow Repository: https://github.com/python-pillow/Pillow
