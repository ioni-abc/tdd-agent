# ClassEval_45

## Skeleton (what the agent sees)

```python
from PIL import Image, ImageEnhance

class ImageProcessor:
    """
    This is a class to process image, including loading, saving, resizing, rotating, and adjusting the brightness of images.
    """

    def __init__(self):
        """
        Initialize self.image
        """
        self.image = None

    def load_image(self, image_path):
        """
        Use Image util in PIL to open a image
        :param image_path: str, path of image that is to be
        >>> processor.load_image('test.jpg')
        >>> processor.image
        <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x194F2412A48>
        """

    def save_image(self, save_path):
        """
        Save image to a path if image has opened
        :param save_path: str, the path that the image will be saved
        >>> processor.load_image('test.jpg')
        >>> processor.save_image('test2.jpg')
        """

    def resize_image(self, width, height):
        """
        Risize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(300, 300)
        >>> processor.image.width
        300
        >>> processor.image.height
        300
        """

    def rotate_image(self, degrees):
        """
        rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(90)
        """

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        >>> processor.load_image('test.jpg')
        >>> processor.adjust_brightness(0.5)
        """
```

## Method `load_image`

### Docstring

```python
def load_image(self, image_path):
        """
        Use Image util in PIL to open a image
        :param image_path: str, path of image that is to be
        >>> processor.load_image('test.jpg')
        >>> processor.image
        <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x194F2412A48>
        """
```

### Reference code (`solution_code`)

```python
def load_image(self, image_path):
        self.image = Image.open(image_path)
```

### Tests (`ImageProcessorTestLoadImage`)

setUp (runs before each test):

```python
def setUp(self):
    self.processor = ImageProcessor()
    self.image_path = os.path.join(os.path.dirname(__file__), "test.png")
    image = Image.new("RGB", (100, 100), (255, 255, 255))
    image.save(self.image_path)
```

**test_load_image**: `stated`
- reason: The docstring says load_image uses PIL to open the image and the example shows processor.image holding the opened image, so a programmer following it would set self.image and the test's not-None check would pass.

```python
def test_load_image(self):
    self.processor.load_image(self.image_path)
    self.assertIsNotNone(self.processor.image)
```

**test_load_image_2**: `stated`
- reason: The docstring says to open the image at the given path with PIL and that the result is stored on `processor.image`, so a programmer following it would set `self.image` to the opened file, whose size then matches the saved 100x100 image the test checks.

```python
def test_load_image_2(self):
    self.processor.load_image(self.image_path)
    self.assertEqual(self.processor.image.size, (100, 100))
```

**test_load_image_3**: `stated`
- reason: The docstring says to open the image with PIL and store it on the processor as `processor.image`, and a programmer doing that would get an image whose mode is preserved from the file, so the RGB mode check passes.

```python
def test_load_image_3(self):
    self.processor.load_image(self.image_path)
    self.assertEqual(self.processor.image.mode, "RGB")
```

**test_load_image_4**: `stated`
- reason: The docstring says to open the image with PIL, and a programmer doing that would store a PIL image whose format comes from the file, so the test's format check follows from the described behaviour.

```python
def test_load_image_4(self):
    self.processor.load_image(self.image_path)
    self.assertEqual(self.processor.image.format, "PNG")
```

**test_load_image_5**: `stated`
- reason: The docstring says to open the image with PIL and shows the result as `processor.image`, so a programmer would write `self.image = Image.open(image_path)`, which sets `filename` to the given path.

```python
def test_load_image_5(self):
    self.processor.load_image(self.image_path)
    self.assertEqual(self.processor.image.filename, self.image_path)
```

## Method `save_image`

### Docstring

```python
def save_image(self, save_path):
        """
        Save image to a path if image has opened
        :param save_path: str, the path that the image will be saved
        >>> processor.load_image('test.jpg')
        >>> processor.save_image('test2.jpg')
        """
```

### Reference code (`solution_code`)

```python
def save_image(self, save_path):
        if self.image:
            self.image.save(save_path)
```

### Tests (`ImageProcessorTestSaveImage`)

setUp (runs before each test):

```python
def setUp(self):
    self.processor = ImageProcessor()
    self.image_path = os.path.join(os.path.dirname(__file__), "test.png")
    image = Image.new("RGB", (100, 100), (255, 255, 255))
    image.save(self.image_path)
```

**test_save_image**: `stated`
- reason: The docstring says save_image writes the loaded image to the given path when one has been opened, which is exactly what the test checks by loading an image, saving it, and reopening the saved file.

```python
def test_save_image(self):
    save_path = os.path.join(os.path.dirname(__file__), "test_save.png")
    self.processor.load_image(self.image_path)
    self.processor.save_image(save_path)
    saved_image = Image.open(save_path)
    self.assertIsNotNone(saved_image)
```

**test_save_image_2**: `stated`
- reason: The docstring says the image is saved to the given path once an image has been opened, which is exactly what the test does before checking the saved file's dimensions.

```python
def test_save_image_2(self):
    save_path = os.path.join(os.path.dirname(__file__), "test_save.png")
    self.processor.load_image(self.image_path)
    self.processor.save_image(save_path)
    saved_image = Image.open(save_path)
    self.assertEqual(saved_image.size, (100, 100))
```

**test_save_image_3**: `stated`
- reason: The docstring says to save the loaded image to the given path, so a programmer would write the file and the saved file's mode will match the loaded RGB image, which is what the test checks.

```python
def test_save_image_3(self):
    save_path = os.path.join(os.path.dirname(__file__), "test_save.png")
    self.processor.load_image(self.image_path)
    self.processor.save_image(save_path)
    saved_image = Image.open(save_path)
    self.assertEqual(saved_image.mode, "RGB")
```

**test_save_image_4**: `stated`
- reason: The docstring says to save the loaded image to the given path, and the test only checks that a `.png` path produces a PNG file, which any standard save-to-path implementation does.

```python
def test_save_image_4(self):
    save_path = os.path.join(os.path.dirname(__file__), "test_save.png")
    self.processor.load_image(self.image_path)
    self.processor.save_image(save_path)
    saved_image = Image.open(save_path)
    self.assertEqual(saved_image.format, "PNG")
```

**test_save_image_5**: `stated`
- reason: The docstring says to save the loaded image to the given path, which is exactly what the test checks by reopening the saved file at that path and confirming its filename.

```python
def test_save_image_5(self):
    save_path = os.path.join(os.path.dirname(__file__), "test_save.png")
    self.processor.load_image(self.image_path)
    self.processor.save_image(save_path)
    saved_image = Image.open(save_path)
    self.assertEqual(saved_image.filename, save_path)
```

## Method `resize_image`

### Docstring

```python
def resize_image(self, width, height):
        """
        Risize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(300, 300)
        >>> processor.image.width
        300
        >>> processor.image.height
        300
        """
```

### Reference code (`solution_code`)

```python
def resize_image(self, width, height):
        if self.image:
            self.image = self.image.resize((width, height))
```

### Tests (`ImageProcessorTestResizeImage`)

setUp (runs before each test):

```python
def setUp(self):
    self.processor = ImageProcessor()
    self.image_path = os.path.join(os.path.dirname(__file__), "test.png")
    image = Image.new("RGB", (100, 100), (255, 255, 255))
    image.save(self.image_path)
```

**test_resize_image**: `stated`
- reason: The docstring says the image is resized to the given target width and height when one is open, which is exactly what the test checks by comparing the image size to (30, 15).

```python
def test_resize_image(self):
    self.processor.load_image(self.image_path)
    self.processor.resize_image(30, 15)
    self.assertEqual(self.processor.image.size, (30, 15))
```

**test_resize_image_2**: `stated`
- reason: The docstring says to resize the loaded image to the given width and height, and a standard resize keeps the image's color mode, so a programmer following it would leave the mode as "RGB" and pass.

```python
def test_resize_image_2(self):
    self.processor.load_image(self.image_path)
    self.processor.resize_image(30, 15)
    self.assertEqual(self.processor.image.mode, "RGB")
```

**test_resize_image_3**: `unstated`
- reason: The test expects the image's `format` attribute to be None after resizing, which is a side effect of PIL creating a new image object, but the docstring never mentions format, so an implementation that preserves the format would fail.
- missing: The docstring should say whether the image's file-format metadata is kept or discarded after resizing, and if it is discarded, that the result has no format value.

```python
def test_resize_image_3(self):
    self.processor.load_image(self.image_path)
    self.processor.resize_image(30, 15)
    self.assertEqual(self.processor.image.format, None)
```

**test_resize_image_4**: `unstated`
- reason: The docstring only says the image is resized to the given width and height, so a programmer would not know the test expects the color mode to remain RGB, though a PIL resize would naturally preserve it.
- missing: The docstring should state that resizing changes only the dimensions and keeps the image's existing color mode (e.g., RGB stays RGB).

```python
def test_resize_image_4(self):
    self.processor.load_image(self.image_path)
    self.processor.resize_image(40, 20)
    self.assertEqual(self.processor.image.mode, "RGB")
```

**test_resize_image_5**: `unstated`
- reason: The docstring only says the image is resized to the given width and height, so it does not say whether the resized image keeps the original format, and the test asserts that the format becomes None.
- missing: The docstring should state whether the resized image keeps the source file's metadata such as its format, or whether resizing produces an image with no format attached.

```python
def test_resize_image_5(self):
    self.processor.load_image(self.image_path)
    self.processor.resize_image(50, 25)
    self.assertEqual(self.processor.image.format, None)
```

## Method `rotate_image`

### Docstring

```python
def rotate_image(self, degrees):
        """
        rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(90)
        """
```

### Reference code (`solution_code`)

```python
def rotate_image(self, degrees):
        if self.image:
            self.image = self.image.rotate(degrees)
```

### Tests (`ImageProcessorTestRotateImage`)

setUp (runs before each test):

```python
def setUp(self):
    self.processor = ImageProcessor()
    self.image_path = os.path.join(os.path.dirname(__file__), "test.png")
    image = Image.new("RGB", (100, 100), (255, 255, 255))
    image.save(self.image_path)
```

**test_rotate_image**: `stated`
- reason: The docstring says rotate the image by the given degrees if an image has been opened, which is exactly what the test checks: load an image, rotate by 90, and compare against a 90-degree rotation of the original.

```python
def test_rotate_image(self):
    self.processor.load_image(self.image_path)
    original_image = self.processor.image
    self.processor.rotate_image(90)
    self.assertTrue(ImageChops.difference(original_image.rotate(90), self.processor.image).getbbox() is None)
```

**test_rotate_image_2**: `stated`
- reason: The docstring says rotate the opened image by the given degrees, which is exactly what the test checks: it loads an image, rotates it 180 degrees, and compares the result to a 180-degree rotation of the original.

```python
def test_rotate_image_2(self):
    self.processor.load_image(self.image_path)
    original_image = self.processor.image
    self.processor.rotate_image(180)
    self.assertTrue(ImageChops.difference(original_image.rotate(180), self.processor.image).getbbox() is None)
```

**test_rotate_image_3**: `unstated`
- reason: The docstring says to rotate the loaded image by the given degrees, but it does not say the direction, and the test expects the counterclockwise convention that PIL's `rotate` uses, so a clockwise implementation would fail.
- missing: The docstring should state the rotation direction and sign convention (for example, that positive angles rotate counterclockwise as in PIL) and whether the image is expanded to fit the rotated result.

```python
def test_rotate_image_3(self):
    self.processor.load_image(self.image_path)
    original_image = self.processor.image
    self.processor.rotate_image(270)
    self.assertTrue(ImageChops.difference(original_image.rotate(270), self.processor.image).getbbox() is None)
```

**test_rotate_image_4**: `stated`
- reason: The docstring says rotate_image rotates the loaded image by the given degrees, so a programmer would implement a rotation, and a 360-degree rotation of a 100x100 image should leave its pixels unchanged, which is what the test checks.

```python
def test_rotate_image_4(self):
    self.processor.load_image(self.image_path)
    original_image = self.processor.image
    self.processor.rotate_image(360)
    self.assertTrue(ImageChops.difference(original_image.rotate(360), self.processor.image).getbbox() is None)
```

**test_rotate_image_5**: `unstated`
- reason: The docstring says to rotate the image by the given degrees but does not say in which direction or whether the canvas expands, and the test's exact pixel comparison against PIL's default `rotate(45)` depends on those choices.
- missing: The docstring should state the rotation direction (for example counterclockwise, as PIL does), whether the output canvas is enlarged to fit the rotated image or keeps the original size, and what fills the uncovered corners.

```python
def test_rotate_image_5(self):
    self.processor.load_image(self.image_path)
    original_image = self.processor.image
    self.processor.rotate_image(45)
    self.assertTrue(ImageChops.difference(original_image.rotate(45), self.processor.image).getbbox() is None)
```

## Method `adjust_brightness`

### Docstring

```python
def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        >>> processor.load_image('test.jpg')
        >>> processor.adjust_brightness(0.5)
        """
```

### Reference code (`solution_code`)

```python
def adjust_brightness(self, factor):
        if self.image:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)
```

### Tests (`ImageProcessorTestAdjustBrightness`)

setUp (runs before each test):

```python
def setUp(self):
    self.processor = ImageProcessor()
    self.image_path = os.path.join(os.path.dirname(__file__), "test.png")
    image = Image.new("RGB", (100, 100), (255, 255, 255))
    image.save(self.image_path)
```

**test_adjust_brightness**: `stated`
- reason: The docstring defines the factor so that 0.0 gives black and 1.0 gives the original image, which is the semantics of PIL's `ImageEnhance.Brightness`, so a programmer following it would produce the same output the test compares against.

```python
def test_adjust_brightness(self):
    self.processor.load_image(self.image_path)
    enhancer = ImageEnhance.Brightness(Image.open(self.image_path))
    expected_image = enhancer.enhance(0.3)
    self.processor.adjust_brightness(0.3)
    self.assertTrue(ImageChops.difference(expected_image, self.processor.image).getbbox() is None)
```

**test_adjust_brightness_2**: `stated`
- reason: The docstring defines the factor so that 0.0 gives black, 1.0 gives the original, and 0.5 falls between them, which is the scaling that PIL's ImageEnhance.Brightness applies and that this test compares against.

```python
def test_adjust_brightness_2(self):
    self.processor.load_image(self.image_path)
    enhancer = ImageEnhance.Brightness(Image.open(self.image_path))
    expected_image = enhancer.enhance(0.5)
    self.processor.adjust_brightness(0.5)
    self.assertTrue(ImageChops.difference(expected_image, self.processor.image).getbbox() is None)
```

**test_adjust_brightness_3**: `stated`
- reason: The docstring defines the factor as a linear brightness scale (0.0 black, 1.0 original), which is what the test checks at 0.7 on a white image, and a programmer would implement it with PIL's brightness enhancer as the reference does.

```python
def test_adjust_brightness_3(self):
    self.processor.load_image(self.image_path)
    enhancer = ImageEnhance.Brightness(Image.open(self.image_path))
    expected_image = enhancer.enhance(0.7)
    self.processor.adjust_brightness(0.7)
    self.assertTrue(ImageChops.difference(expected_image, self.processor.image).getbbox() is None)
```

**test_adjust_brightness_4**: `stated`
- reason: The docstring explicitly says a factor of 1.0 gives the original image, which is exactly what this test checks by comparing the processed image against an unchanged enhancement of the loaded image.

```python
def test_adjust_brightness_4(self):
    self.processor.load_image(self.image_path)
    enhancer = ImageEnhance.Brightness(Image.open(self.image_path))
    expected_image = enhancer.enhance(1.0)
    self.processor.adjust_brightness(1.0)
    self.assertTrue(ImageChops.difference(expected_image, self.processor.image).getbbox() is None)
```

**test_adjust_brightness_5**: `stated`
- reason: The docstring defines the factor so that 0.0 gives black and 1.0 gives the original, which implies multiplicative brightness scaling, so a programmer would produce the same result as the test's PIL-based expected image for factor 1.5.

```python
def test_adjust_brightness_5(self):
    self.processor.load_image(self.image_path)
    enhancer = ImageEnhance.Brightness(Image.open(self.image_path))
    expected_image = enhancer.enhance(1.5)
    self.processor.adjust_brightness(1.5)
    self.assertTrue(ImageChops.difference(expected_image, self.processor.image).getbbox() is None)
```

## Tests in no method's test class

### `ImageProcessorTestMain`

setUp (runs before each test):

```python
def setUp(self):
    self.processor = ImageProcessor()
    self.image_path = os.path.join(os.path.dirname(__file__), "test.png")
    image = Image.new("RGB", (100, 100), (255, 255, 255))
    image.save(self.image_path)
```

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    self.processor.load_image(self.image_path)
    self.assertIsNotNone(self.processor.image)

    enhancer = ImageEnhance.Brightness(Image.open(self.image_path))
    expected_image = enhancer.enhance(0.4)
    self.processor.adjust_brightness(0.4)
    self.assertTrue(ImageChops.difference(expected_image, self.processor.image).getbbox() is None)

    self.processor.resize_image(30, 15)
    self.assertEqual(self.processor.image.size, (30, 15))

    original_image = self.processor.image
    self.processor.rotate_image(90)
    self.assertTrue(ImageChops.difference(original_image.rotate(90), self.processor.image).getbbox() is None)

    save_path = os.path.join(os.path.dirname(__file__), "test_save.png")
    self.processor.save_image(save_path)
    saved_image = Image.open(save_path)
    self.assertIsNotNone(saved_image)
    saved_image.close()
```
