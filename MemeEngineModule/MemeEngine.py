"""Responsible for manipulating and drawing text onto images."""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
from datetime import datetime
import shutil
import math


class MemeEngine():
    """Load, resize manipulate and save an image."""

    def __init__(self, output_dir):
        """Set up an instance object with the output directory."""
        if type(output_dir) is not str:
            raise Exception("Output dir is not of type string.")
        self.output_dir = str(output_dir)

    def handle_linebreaks(self, x, y, max_characters, drawing, text):
        """
        Handle the linebreaks of text and author.
        :param x: (int) x coordinate of the text.
        :param y: (int) y coordinate of the text.
        :param max_characters: (int) space available in the image.
        :param drawing: drawing context on image object
        :param text: (string) text to be written on the image.
        :return: drawing object, new y coordinate
        """
        # calculate how many lines are needed:
        lines = math.ceil(len(text) / max_characters)
        # load the font
        lilita = ImageFont.truetype("./fonts/LilitaOne-Regular.ttf", 25)
        for i in range(lines):
            drawing.multiline_text((x, y+(i*20)),
                                   text[max_characters*i:max_characters*(i+1)],
                                   font=lilita, fill=(255, 255, 255))
        # calculate the y coordinate where the author starts
        y = y+(lines*20)+25
        return drawing, y

    def draw_text(self, image, text, author):
        """Write the text on the image."""

        x = 20
        y = 80
        max_characters = 50

        # get a drawing context
        drawing = ImageDraw.Draw(image)
        drawing, y = self.handle_linebreaks(x, y, max_characters,
                                            drawing, text)
        drawing, y = self.handle_linebreaks(x, y, max_characters,
                                            drawing, author)

        return drawing

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Add the quote to the image and save it.

        :param img_path: (str) path to image to load.
        :param text: (str) The quote body to be put on the image.
        :param author: (str) The author to be put beneath the quote body.
        :param width: (int) Maximum allowed width of the image.
                    Everything above will be downscaled.
        :return: Success string were the image is saved.
        """
        # avoid meme buildup by deleting and recreating the static folder
        shutil.rmtree('./static')
        os.mkdir("./static")

        im = Image.open(img_path)
        # get the width of the image
        img_width = im.size[0]

        # resize if image is too wide
        if img_width > width:
            factor = width / img_width
            im = im.resize((int(im.size[0] * factor),
                            int(im.size[1] * factor)))

        drawing = self.draw_text(im, text, author)
        filename = f"/meme_{datetime.now().strftime('%H_%M_%S')}.jpg"
        meme_path = self.output_dir + filename
        try:
            im.save(meme_path)
        except OSError:
            os.mkdir(self.output_dir)
            im.save(meme_path)

        return meme_path
