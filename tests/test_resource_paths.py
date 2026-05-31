import unittest

from app.utils.paths import image_path, model_path, seed_data_path


class ResourcePathTests(unittest.TestCase):
    def test_core_resources_exist(self):
        self.assertTrue(image_path("hnd1.jpg").exists())
        self.assertTrue(image_path("neural2.jpeg").exists())
        self.assertTrue(model_path("hrmodel.model").exists())
        self.assertTrue(model_path("lb.pickle").exists())
        self.assertTrue(seed_data_path("Form1.db").exists())


if __name__ == "__main__":
    unittest.main()
