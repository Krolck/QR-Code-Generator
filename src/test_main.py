import tempfile
import unittest
from pathlib import Path

from main import build_output_path, validate_url


class MainModuleTests(unittest.TestCase):
    def test_validate_url_rejects_blank_and_non_http_inputs(self):
        with self.assertRaises(ValueError) as blank_exc:
            validate_url("   ")
        self.assertIn("must not be blank", str(blank_exc.exception))

        with self.assertRaises(ValueError) as scheme_exc:
            validate_url("www.reject.com")
        self.assertIn("must begin with \"http://\" or \"https://\"", str(scheme_exc.exception))

    def test_build_output_path_appends_counter_for_duplicate_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            first_path = build_output_path("https://hirewheel.ai", output_dir)
            first_path.touch()

            second_path = build_output_path("https://hirewheel.ai", output_dir)
            self.assertNotEqual(first_path, second_path)
            self.assertTrue(str(second_path).endswith("hirewheel_ai_1.png"))

            second_path.touch()
            third_path = build_output_path("https://hirewheel.ai", output_dir)
            self.assertTrue(str(third_path).endswith("hirewheel_ai_2.png"))


if __name__ == "__main__":
    unittest.main()
