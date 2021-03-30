"""Responsible for manipulating and drawing text onto images."""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class MemeEngine():
    """Load, resize manipulate and save an image."""

    def __init__(self, output_dir):
        """Set up an instance object with the output directory."""
        if type(output_dir) is not str:
            raise Exception("Output dir is not of type string.")
        self.output_dir = str(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Add the quote to the image and save it.

        :param img_path: (str) path to image to load.
        :param text: (str) The quote body to be put on the image.
        :param author: (str) The author to be put beneath the quote body.
        :param width: (int) Maximum allowed width of the image. Everything above will be downscaled.
        :return: Success string were the image is saved.
        """
        im = Image.open(img_path)
        # get the width of the image
        img_width = im.size[0]

        # resize if image is too wide
        if img_width > width:
            factor = width / img_width
            im = im.resize((im.size[0] * factor, im.size[1] * factor))

        # load the font
        lilita = ImageFont.truetype("./fonts/LilitaOne-Regular.ttf", 25)
        # get a drawing context
        drawing = ImageDraw.Draw(im)
        drawing.multiline_text((20, 80), text, font=lilita, fill=(255, 255, 255))
        drawing.multiline_text((20, 110), author, font=lilita, fill=(255, 255, 255))

        im.save(self.output_dir+"/meme.jpg")

        return f"Saved the image to '{self.output_dir}'"
