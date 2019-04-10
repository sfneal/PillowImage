import os
import unittest

from looptools import Timer

from PillowImage import PillowImage, img_adjust
from tests import *


class TestPillowImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.img_path = img_path
        cls.wtrmrk_path = wtr_path
        cls.pdf = None

    def setUp(self):
        self.draw = None

    def tearDown(self):
        self.draw.cleanup()

    @Timer.decorator
    def test_draw_text(self):
        """Draw text onto an image."""
        self.draw = PillowImage()
        self.draw.draw_text('Here is the first text', y=10, opacity=50)
        self.draw.draw_text('Here is the second text', y=50, opacity=50)
        d = self.draw.save(destination=test_data_dir, file_name='draw_text')

        # Assert file exists
        self.assertTrue(os.path.exists(d))
        return d

    @Timer.decorator
    def test_draw_img(self):
        """Draw text onto an image."""
        self.draw = PillowImage()
        self.draw.draw_img(self.img_path)
        self.draw.draw_img(self.wtrmrk_path, opacity=0.08, rotate=30)
        d = self.draw.save(destination=test_data_dir, file_name='draw_img')

        # Assert file exists
        self.assertTrue(os.path.exists(d))
        return d

    @Timer.decorator
    def test_draw_img_overlay(self):
        """Draw text onto an image."""
        self.draw = PillowImage(img=self.img_path)
        self.draw.draw_img(self.wtrmrk_path, opacity=0.08, rotate=30)
        d = self.draw.save(destination=test_data_dir, file_name='draw_img_overlay')

        # Assert file exists
        self.assertTrue(os.path.exists(d))
        return d

    @Timer.decorator
    def test_draw_img_centered(self):
        """Draw text onto an image."""
        self.draw = PillowImage(img=self.img_path)
        self.draw.draw_img(self.wtrmrk_path, opacity=0.08, rotate=30, x='center', y='center')
        d = self.draw.save(destination=test_data_dir, file_name='draw_img_centered')

        # Assert file exists
        self.assertTrue(os.path.exists(d))
        return d

    @Timer.decorator
    def test_draw_img_negbound(self):
        """Draw text onto an image."""
        self.draw = PillowImage(img=self.img_path)
        self.draw.draw_img(self.wtrmrk_path, opacity=0.08, rotate=30, x=-2000, y=-2000)
        d = self.draw.save(destination=test_data_dir, file_name='draw_img_negbound')

        # Assert file exists
        self.assertTrue(os.path.exists(d))
        return d

    @Timer.decorator
    def test_draw_img_percentage(self):
        """Draw text onto an image."""
        self.draw = PillowImage(img=self.img_path)
        self.draw.draw_img(self.wtrmrk_path, opacity=0.08, rotate=30, x=.5, y=.1)
        d = self.draw.save(destination=test_data_dir, file_name='draw_img_percentage')

        # Assert file exists
        self.assertTrue(os.path.exists(d))
        return d

    @Timer.decorator
    def test_draw_img_resized(self):
        """Draw text onto an image."""
        longest_side = 500
        self.draw = PillowImage(img=self.img_path)
        self.draw.draw_img(self.wtrmrk_path, opacity=0.08, rotate=30)
        self.draw.resize(longest_side)
        d = self.draw.save(destination=test_data_dir, file_name='draw_img_resized')

        # Assert file exists
        self.assertTrue(os.path.exists(d))

        # Assert actual longest edge is equal to target longest edge
        self.assertEqual(longest_side, self.draw.longest_side)
        return d

    @Timer.decorator
    def test_draw_img_resize_width(self):
        """Draw text onto an image."""
        width = 300
        self.draw = PillowImage(img=self.img_path)
        self.draw.resize_width(width)
        d = self.draw.save(destination=test_data_dir, file_name='draw_img_resized_width')

        # Assert file exists
        self.assertTrue(os.path.exists(d))

        # Assert actual longest edge is equal to target longest edge
        self.assertEqual(width, self.draw.width)
        return d

    @Timer.decorator
    def test_draw_img_resize_height(self):
        """Draw text onto an image."""
        height = 300
        self.draw = PillowImage(img=self.img_path)
        self.draw.resize_height(height)
        d = self.draw.save(destination=test_data_dir, file_name='draw_img_resized_height')

        # Assert file exists
        self.assertTrue(os.path.exists(d))

        # Assert actual longest edge is equal to target longest edge
        self.assertEqual(height, self.draw.height)
        return d

    @Timer.decorator
    def test_rotate(self):
        """Draw text onto an image."""
        self.draw = PillowImage()
        self.draw.draw_img(self.img_path)
        self.draw.rotate(30)
        d = self.draw.save(destination=test_data_dir, file_name='rotate')

        # Assert file exists
        self.assertTrue(os.path.exists(d))
        return d

    @Timer.decorator
    def test_size(self):
        """Draw text onto an image."""
        self.draw = PillowImage(img=self.img_path)
        size = self.draw.size
        d = self.draw.save(destination=test_data_dir, file_name='size')

        # Assert file exists
        self.assertTrue(os.path.exists(d))

        # Assert image size is correct
        self.assertIsInstance(size, tuple)
        self.assertTrue(size == (2706, 2226))
        return d

    @Timer.decorator
    def test_width(self):
        """Draw text onto an image."""
        self.draw = PillowImage(img=self.img_path)
        width = self.draw.width
        d = self.draw.save(destination=test_data_dir, file_name='width')

        # Assert file exists
        self.assertTrue(os.path.exists(d))

        # Assert image size is correct
        self.assertTrue(width == 2706)
        return d

    @Timer.decorator
    def test_height(self):
        """Draw text onto an image."""
        self.draw = PillowImage(img=self.img_path)
        height = self.draw.height
        d = self.draw.save(destination=test_data_dir, file_name='height')

        # Assert file exists
        self.assertTrue(os.path.exists(d))

        # Assert image size is correct
        self.assertTrue(height == 2226)
        return d
    

class TestPillowImageUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.img_path = img_path
        cls.wtrmrk_path = wtr_path
        cls.pdf = None

    def setUp(self):
        self.image = None

    def tearDown(self):
        os.remove(self.image)

    @Timer.decorator
    def test_img_adjust_rotate(self):
        """Test the function 'img_rotate.'"""
        self.image = img_adjust(self.wtrmrk_path, rotate=30, fit=1)

        # Assert file exists
        self.assertTrue(os.path.exists(self.image))
        return self.image


if __name__ == '__main__':
    unittest.main()
