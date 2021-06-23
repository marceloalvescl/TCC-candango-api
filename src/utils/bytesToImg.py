
import PIL.Image as Image
import io


def bytesToPNG(bytes):
    image = Image.open(io.BytesIO(bytes))
    img_io = io.BytesIO()
    image.save(img_io, "PNG", quality=70)
    img_io.seek(0)
    return img_io