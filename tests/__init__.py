import os


TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TEST_RESULTS_DIR = os.path.join(os.path.dirname(__file__), 'results')

IMG_NAME = 'floor plan.png'
IMG_PATH = os.path.join(TEST_DATA_DIR, IMG_NAME)

IMG_NAME_JPEG = 'elevation.jpg'
IMG_PATH_JPEG = os.path.join(TEST_DATA_DIR, IMG_NAME_JPEG)

WTR_NAME = 'watermark.png'
WTR_PATH = os.path.join(TEST_DATA_DIR, WTR_NAME)


__all__ = ['IMG_PATH', 'WTR_PATH', 'TEST_DATA_DIR', 'TEST_RESULTS_DIR', 'IMG_NAME_JPEG', 'IMG_PATH_JPEG']
