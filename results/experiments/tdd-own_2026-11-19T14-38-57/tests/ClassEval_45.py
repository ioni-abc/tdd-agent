import unittest


import unittest

import os

import tempfile

from PIL import Image, ImageEnhance

class AgentTest_load_image(unittest.TestCase):

    def setUp(self):
        self.processor = ImageProcessor()
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp_dir = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def _make_image(self, name, size=(40, 30), mode='RGB', color=(255, 0, 0), fmt=None):
        path = os.path.join(self.tmp_dir, name)
        img = Image.new(mode, size, color)
        if fmt is None:
            img.save(path)
        else:
            img.save(path, format=fmt)
        return path

    def test_load_image_1(self):
        # load_image should open the file with PIL and store the resulting image in self.image
        path = self._make_image('sample.png')
        self.processor.load_image(path)
        self.assertIsInstance(self.processor.image, Image.Image)

    def test_load_image_2(self):
        # The loaded image should have the same width and height as the file on disk
        path = self._make_image('sized.png', size=(120, 80))
        self.processor.load_image(path)
        self.assertEqual(self.processor.image.width, 120)
        self.assertEqual(self.processor.image.height, 80)

    def test_load_image_3(self):
        # A JPEG file should be opened as a JPEG image in RGB mode, as in the docstring example
        path = self._make_image('photo.jpg', size=(64, 48), mode='RGB', fmt='JPEG')
        self.processor.load_image(path)
        self.assertEqual(self.processor.image.format, 'JPEG')
        self.assertEqual(self.processor.image.mode, 'RGB')
        self.assertEqual(self.processor.image.size, (64, 48))

    def test_load_image_4(self):
        # The image mode should reflect the mode of the file that was opened
        path = self._make_image('gray.png', size=(20, 10), mode='L', color=128)
        self.processor.load_image(path)
        self.assertEqual(self.processor.image.mode, 'L')
        self.assertEqual(self.processor.image.format, 'PNG')

    def test_load_image_5(self):
        # Loading a second image should replace the previously loaded image
        first = self._make_image('first.png', size=(30, 30))
        second = self._make_image('second.png', size=(50, 70))
        self.processor.load_image(first)
        self.assertEqual(self.processor.image.size, (30, 30))
        self.processor.load_image(second)
        self.assertEqual(self.processor.image.width, 50)
        self.assertEqual(self.processor.image.height, 70)

import unittest

import os

import tempfile

from PIL import Image, ImageEnhance

class AgentTest_save_image(unittest.TestCase):

    def setUp(self):
        self.processor = ImageProcessor()
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp_dir = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def _make_image(self, name, size=(40, 30), mode='RGB', color=(255, 0, 0), fmt=None):
        path = os.path.join(self.tmp_dir, name)
        img = Image.new(mode, size, color)
        if fmt is None:
            img.save(path)
        else:
            img.save(path, format=fmt)
        return path

    def test_save_image_1(self):
        # After an image has been loaded, save_image should create a file at save_path
        src = self._make_image('src.png', size=(40, 30))
        dst = os.path.join(self.tmp_dir, 'saved.png')
        self.processor.load_image(src)
        self.processor.save_image(dst)
        self.assertTrue(os.path.exists(dst))

    def test_save_image_2(self):
        # The saved file should contain the loaded image with the same width and height
        src = self._make_image('src.png', size=(120, 80))
        dst = os.path.join(self.tmp_dir, 'saved_size.png')
        self.processor.load_image(src)
        self.processor.save_image(dst)
        reopened = Image.open(dst)
        self.assertEqual(reopened.size, (120, 80))
        reopened.close()

    def test_save_image_3(self):
        # The saved file should keep the mode of the loaded image
        src = self._make_image('gray.png', size=(20, 10), mode='L', color=128)
        dst = os.path.join(self.tmp_dir, 'gray_saved.png')
        self.processor.load_image(src)
        self.processor.save_image(dst)
        reopened = Image.open(dst)
        self.assertEqual(reopened.mode, 'L')
        reopened.close()

    def test_save_image_4(self):
        # Saving to a .jpg path should produce a JPEG file, as in the docstring example
        src = self._make_image('src.png', size=(64, 48))
        dst = os.path.join(self.tmp_dir, 'test2.jpg')
        self.processor.load_image(src)
        self.processor.save_image(dst)
        reopened = Image.open(dst)
        self.assertEqual(reopened.format, 'JPEG')
        reopened.close()

    def test_save_image_5(self):
        # If no image has been opened, save_image should not create a file
        dst = os.path.join(self.tmp_dir, 'nothing_loaded.png')
        self.assertIsNone(self.processor.image)
        try:
            self.processor.save_image(dst)
        except Exception:
            pass
        self.assertFalse(os.path.exists(dst))

import unittest

import os

import tempfile

from PIL import Image, ImageEnhance

class AgentTest_resize_image(unittest.TestCase):

    def setUp(self):
        self.processor = ImageProcessor()
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp_dir = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def _make_image(self, name, size=(40, 30), mode='RGB', color=(255, 0, 0), fmt=None):
        path = os.path.join(self.tmp_dir, name)
        img = Image.new(mode, size, color)
        if fmt is None:
            img.save(path)
        else:
            img.save(path, format=fmt)
        return path

    def test_resize_image_1(self):
        # As in the docstring example, resizing a loaded image to 300x300 should give width 300 and height 300
        path = self._make_image('square.png', size=(40, 30))
        self.processor.load_image(path)
        self.processor.resize_image(300, 300)
        self.assertEqual(self.processor.image.width, 300)
        self.assertEqual(self.processor.image.height, 300)

    def test_resize_image_2(self):
        # Width and height are independent targets; a non-square shrink should give exactly the requested size
        path = self._make_image('shrink.png', size=(120, 80))
        self.processor.load_image(path)
        self.processor.resize_image(20, 10)
        self.assertEqual(self.processor.image.size, (20, 10))

    def test_resize_image_3(self):
        # Enlarging an image should also yield exactly the requested width and height
        path = self._make_image('enlarge.png', size=(40, 30))
        self.processor.load_image(path)
        self.processor.resize_image(200, 150)
        self.assertEqual(self.processor.image.width, 200)
        self.assertEqual(self.processor.image.height, 150)
        self.assertIsInstance(self.processor.image, Image.Image)

    def test_resize_image_4(self):
        # The resized image is the one held by the processor, so saving afterwards should write the new dimensions
        src = self._make_image('src.png', size=(40, 30))
        dst = os.path.join(self.tmp_dir, 'resized_saved.png')
        self.processor.load_image(src)
        self.processor.resize_image(64, 48)
        self.processor.save_image(dst)
        reopened = Image.open(dst)
        self.assertEqual(reopened.size, (64, 48))
        reopened.close()

    def test_resize_image_5(self):
        # If no image has been opened, resize_image should leave self.image as None
        self.assertIsNone(self.processor.image)
        try:
            self.processor.resize_image(300, 300)
        except Exception:
            pass
        self.assertIsNone(self.processor.image)

import os

import tempfile

from PIL import Image, ImageEnhance

class AgentTest_rotate_image(unittest.TestCase):

    def setUp(self):
        self.processor = ImageProcessor()
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp_dir = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def _make_image(self, name, size=(40, 30), mode='RGB', color=(255, 0, 0), fmt=None):
        path = os.path.join(self.tmp_dir, name)
        img = Image.new(mode, size, color)
        if fmt is None:
            img.save(path)
        else:
            img.save(path, format=fmt)
        return path

    def test_rotate_image_1(self):
        # Rotating a loaded image by 90 degrees (either direction) should swap its width and height
        path = self._make_image('rot90.png', size=(40, 30))
        self.processor.load_image(path)
        self.processor.rotate_image(90)
        self.assertEqual(self.processor.image.size, (30, 40))

    def test_rotate_image_2(self):
        # Rotating by 180 degrees should keep the image as a PIL image with unchanged dimensions
        path = self._make_image('rot180.png', size=(120, 80))
        self.processor.load_image(path)
        self.processor.rotate_image(180)
        self.assertIsInstance(self.processor.image, Image.Image)
        self.assertEqual(self.processor.image.size, (120, 80))

    def test_rotate_image_3(self):
        # A 180 degree rotation moves the top-left pixel to the bottom-right corner, regardless of direction
        path = os.path.join(self.tmp_dir, 'corner.png')
        img = Image.new('RGB', (40, 30), (0, 0, 255))
        img.putpixel((0, 0), (255, 0, 0))
        img.save(path)
        self.processor.load_image(path)
        self.processor.rotate_image(180)
        self.assertEqual(self.processor.image.getpixel((39, 29)), (255, 0, 0))

    def test_rotate_image_4(self):
        # A full turn given as a float (360.0) should leave the image dimensions unchanged
        path = self._make_image('full_turn.png', size=(64, 48))
        self.processor.load_image(path)
        self.processor.rotate_image(360.0)
        self.assertEqual(self.processor.image.size, (64, 48))

    def test_rotate_image_5(self):
        # If no image has been opened, rotate_image should leave self.image as None
        self.assertIsNone(self.processor.image)
        try:
            self.processor.rotate_image(90)
        except Exception:
            pass
        self.assertIsNone(self.processor.image)

import unittest

import os

import tempfile

from PIL import Image, ImageEnhance

class AgentTest_adjust_brightness(unittest.TestCase):

    def setUp(self):
        self.processor = ImageProcessor()
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp_dir = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def _make_image(self, name, size=(40, 30), mode='RGB', color=(255, 0, 0), fmt=None):
        path = os.path.join(self.tmp_dir, name)
        img = Image.new(mode, size, color)
        if fmt is None:
            img.save(path)
        else:
            img.save(path, format=fmt)
        return path

    def test_adjust_brightness_1(self):
        # A factor of 0.0 should give a black image
        path = self._make_image('bright.png', size=(40, 30), color=(200, 100, 50))
        self.processor.load_image(path)
        self.processor.adjust_brightness(0.0)
        self.assertEqual(self.processor.image.getextrema(), ((0, 0), (0, 0), (0, 0)))

    def test_adjust_brightness_2(self):
        # A factor of 1.0 should leave the image unchanged
        path = self._make_image('same.png', size=(40, 30), color=(200, 100, 50))
        self.processor.load_image(path)
        before = list(self.processor.image.getdata())
        self.processor.adjust_brightness(1.0)
        after = list(self.processor.image.getdata())
        self.assertEqual(after, before)

    def test_adjust_brightness_3(self):
        # A factor between 0.0 and 1.0 should make the image darker than the original
        path = self._make_image('dim.png', size=(40, 30), color=(200, 100, 50))
        self.processor.load_image(path)
        original = self.processor.image.getpixel((0, 0))
        self.processor.adjust_brightness(0.5)
        dimmed = self.processor.image.getpixel((0, 0))
        for new_value, old_value in zip(dimmed, original):
            self.assertLessEqual(new_value, old_value)
        self.assertLess(sum(dimmed), sum(original))

    def test_adjust_brightness_4(self):
        # Adjusting brightness should keep the image size and mode
        path = self._make_image('gray.png', size=(20, 10), mode='L', color=128)
        self.processor.load_image(path)
        self.processor.adjust_brightness(0.5)
        self.assertIsInstance(self.processor.image, Image.Image)
        self.assertEqual(self.processor.image.size, (20, 10))
        self.assertEqual(self.processor.image.mode, 'L')

    def test_adjust_brightness_5(self):
        # If no image has been opened, adjust_brightness should leave self.image as None
        self.assertIsNone(self.processor.image)
        try:
            self.processor.adjust_brightness(0.5)
        except Exception:
            pass
        self.assertIsNone(self.processor.image)