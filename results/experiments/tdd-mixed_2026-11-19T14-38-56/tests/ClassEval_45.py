import unittest
import os




class ImageProcessorTestLoadImage(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image_path = os.path.join(os.path.dirname(__file__), "test.png")
        image = Image.new("RGB", (100, 100), (255, 255, 255))
        image.save(self.image_path)

    def tearDown(self):
        self.processor.image.close()

    def test_load_image(self):
        self.processor.load_image(self.image_path)
        self.assertIsNotNone(self.processor.image)

    def test_load_image_2(self):
        self.processor.load_image(self.image_path)
        self.assertEqual(self.processor.image.size, (100, 100))

    def test_load_image_3(self):
        self.processor.load_image(self.image_path)
        self.assertEqual(self.processor.image.mode, "RGB")

import os

import unittest

from PIL import Image

class AgentTest_load_image(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image_path = os.path.join(os.path.dirname(__file__), "agent_load_test.png")
        self.second_path = os.path.join(os.path.dirname(__file__), "agent_load_test_second.png")
        Image.new("RGB", (100, 100), (255, 255, 255)).save(self.image_path)
        Image.new("RGB", (50, 80), (0, 0, 0)).save(self.second_path)

    def tearDown(self):
        if self.processor.image is not None:
            self.processor.image.close()
        for path in (self.image_path, self.second_path):
            if os.path.exists(path):
                os.remove(path)

    def test_load_image_1(self):
        self.processor.load_image(self.image_path)
        self.assertEqual(self.processor.image.format, "PNG")

    def test_load_image_2(self):
        self.processor.load_image(self.image_path)
        self.processor.image.close()
        self.processor.load_image(self.second_path)
        self.assertEqual(self.processor.image.size, (50, 80))

class ImageProcessorTestSaveImage(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image_path = os.path.join(os.path.dirname(__file__), "test.png")
        image = Image.new("RGB", (100, 100), (255, 255, 255))
        image.save(self.image_path)

    def tearDown(self):
        self.processor.image.close()

    def test_save_image(self):
        save_path = os.path.join(os.path.dirname(__file__), "test_save.png")
        self.processor.load_image(self.image_path)
        self.processor.save_image(save_path)
        saved_image = Image.open(save_path)
        self.assertIsNotNone(saved_image)

    def test_save_image_2(self):
        save_path = os.path.join(os.path.dirname(__file__), "test_save.png")
        self.processor.load_image(self.image_path)
        self.processor.save_image(save_path)
        saved_image = Image.open(save_path)
        self.assertEqual(saved_image.size, (100, 100))

    def test_save_image_3(self):
        save_path = os.path.join(os.path.dirname(__file__), "test_save.png")
        self.processor.load_image(self.image_path)
        self.processor.save_image(save_path)
        saved_image = Image.open(save_path)
        self.assertEqual(saved_image.mode, "RGB")

import os

from PIL import Image

class AgentTest_save_image(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.source_path = os.path.join(os.path.dirname(__file__), "agent_save_source.png")
        self.output_paths = []
        Image.new("RGB", (20, 20), (255, 0, 0)).save(self.source_path)

    def tearDown(self):
        if self.processor.image is not None:
            self.processor.image.close()
        for path in [self.source_path] + self.output_paths:
            if os.path.exists(path):
                os.remove(path)

    def _output_path(self, name):
        path = os.path.join(os.path.dirname(__file__), name)
        self.output_paths.append(path)
        return path

    def test_save_image_1(self):
        save_path = self._output_path("agent_save_output_1.png")
        self.processor.load_image(self.source_path)
        self.processor.save_image(save_path)
        with Image.open(save_path) as saved_image:
            self.assertEqual(saved_image.convert("RGB").getpixel((5, 5)), (255, 0, 0))

    def test_save_image_2(self):
        save_path = self._output_path("agent_save_output_2.jpg")
        self.processor.load_image(self.source_path)
        self.processor.save_image(save_path)
        with Image.open(save_path) as saved_image:
            self.assertEqual(saved_image.format, "JPEG")

class ImageProcessorTestResizeImage(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image_path = os.path.join(os.path.dirname(__file__), "test.png")
        image = Image.new("RGB", (100, 100), (255, 255, 255))
        image.save(self.image_path)

    def tearDown(self):
        self.processor.image.close()

    def test_resize_image(self):
        self.processor.load_image(self.image_path)
        self.processor.resize_image(30, 15)
        self.assertEqual(self.processor.image.size, (30, 15))

    def test_resize_image_2(self):
        self.processor.load_image(self.image_path)
        self.processor.resize_image(30, 15)
        self.assertEqual(self.processor.image.mode, "RGB")

    def test_resize_image_3(self):
        self.processor.load_image(self.image_path)
        self.processor.resize_image(30, 15)
        self.assertEqual(self.processor.image.format, None)

import os

from PIL import Image

class AgentTest_resize_image(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image_path = os.path.join(os.path.dirname(__file__), "agent_resize_source.png")
        Image.new("RGB", (100, 100), (255, 255, 255)).save(self.image_path)

    def tearDown(self):
        if self.processor.image is not None:
            self.processor.image.close()
        if os.path.exists(self.image_path):
            os.remove(self.image_path)

    def test_resize_image_1(self):
        self.processor.load_image(self.image_path)
        self.processor.resize_image(300, 300)
        self.assertEqual(self.processor.image.width, 300)
        self.assertEqual(self.processor.image.height, 300)

    def test_resize_image_2(self):
        self.processor.load_image(self.image_path)
        self.processor.resize_image(200, 50)
        self.processor.resize_image(20, 80)
        self.assertEqual(self.processor.image.width, 20)
        self.assertEqual(self.processor.image.height, 80)

class ImageProcessorTestRotateImage(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image_path = os.path.join(os.path.dirname(__file__), "test.png")
        image = Image.new("RGB", (100, 100), (255, 255, 255))
        image.save(self.image_path)

    def tearDown(self):
        self.processor.image.close()

    def test_rotate_image(self):
        self.processor.load_image(self.image_path)
        original_image = self.processor.image
        self.processor.rotate_image(90)
        self.assertTrue(ImageChops.difference(original_image.rotate(90), self.processor.image).getbbox() is None)

    def test_rotate_image_2(self):
        self.processor.load_image(self.image_path)
        original_image = self.processor.image
        self.processor.rotate_image(180)
        self.assertTrue(ImageChops.difference(original_image.rotate(180), self.processor.image).getbbox() is None)

    def test_rotate_image_3(self):
        self.processor.load_image(self.image_path)
        original_image = self.processor.image
        self.processor.rotate_image(270)
        self.assertTrue(ImageChops.difference(original_image.rotate(270), self.processor.image).getbbox() is None)

import os

import unittest

from PIL import Image, ImageChops

class AgentTest_rotate_image(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image_path = os.path.join(os.path.dirname(__file__), "agent_rotate_source.png")
        source = Image.new("RGB", (20, 30), (255, 255, 255))
        source.putpixel((0, 0), (255, 0, 0))
        source.putpixel((19, 29), (0, 0, 255))
        source.save(self.image_path)

    def tearDown(self):
        if self.processor.image is not None:
            self.processor.image.close()
        if os.path.exists(self.image_path):
            os.remove(self.image_path)

    def test_rotate_image_1(self):
        self.processor.load_image(self.image_path)
        original_image = self.processor.image.copy()
        self.processor.rotate_image(0)
        self.assertIsNone(ImageChops.difference(original_image, self.processor.image).getbbox())

    def test_rotate_image_2(self):
        self.processor.load_image(self.image_path)
        original_image = self.processor.image.copy()
        self.processor.rotate_image(360.0)
        self.assertIsNone(ImageChops.difference(original_image, self.processor.image).getbbox())

class ImageProcessorTestAdjustBrightness(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image_path = os.path.join(os.path.dirname(__file__), "test.png")
        image = Image.new("RGB", (100, 100), (255, 255, 255))
        image.save(self.image_path)

    def tearDown(self):
        self.processor.image.close()

    def test_adjust_brightness(self):
        self.processor.load_image(self.image_path)
        enhancer = ImageEnhance.Brightness(Image.open(self.image_path))
        expected_image = enhancer.enhance(0.3)
        self.processor.adjust_brightness(0.3)
        self.assertTrue(ImageChops.difference(expected_image, self.processor.image).getbbox() is None)

    def test_adjust_brightness_2(self):
        self.processor.load_image(self.image_path)
        enhancer = ImageEnhance.Brightness(Image.open(self.image_path))
        expected_image = enhancer.enhance(0.5)
        self.processor.adjust_brightness(0.5)
        self.assertTrue(ImageChops.difference(expected_image, self.processor.image).getbbox() is None)

    def test_adjust_brightness_3(self):
        self.processor.load_image(self.image_path)
        enhancer = ImageEnhance.Brightness(Image.open(self.image_path))
        expected_image = enhancer.enhance(0.7)
        self.processor.adjust_brightness(0.7)
        self.assertTrue(ImageChops.difference(expected_image, self.processor.image).getbbox() is None)

import os

import unittest

from PIL import Image, ImageChops

class AgentTest_adjust_brightness(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image_path = os.path.join(os.path.dirname(__file__), "agent_brightness_source.png")
        Image.new("RGB", (20, 20), (200, 100, 50)).save(self.image_path)

    def tearDown(self):
        if self.processor.image is not None:
            self.processor.image.close()
        if os.path.exists(self.image_path):
            os.remove(self.image_path)

    def test_adjust_brightness_1(self):
        self.processor.load_image(self.image_path)
        self.processor.adjust_brightness(0.0)
        self.assertEqual(self.processor.image.convert("RGB").getpixel((5, 5)), (0, 0, 0))
        self.assertIsNone(self.processor.image.convert("RGB").getbbox() and
                          ImageChops.difference(self.processor.image.convert("RGB"),
                                                Image.new("RGB", self.processor.image.size, (0, 0, 0)))
                          .getbbox())

    def test_adjust_brightness_2(self):
        self.processor.load_image(self.image_path)
        original_image = self.processor.image.copy()
        self.processor.adjust_brightness(1.0)
        self.assertIsNone(ImageChops.difference(original_image, self.processor.image).getbbox())