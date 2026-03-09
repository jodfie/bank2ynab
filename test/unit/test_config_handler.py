import os
import tempfile
import unittest
from pathlib import Path

from bank2ynab.config_handler import ConfigHandler


class TestConfigHandlerPaths(unittest.TestCase):
    def setUp(self) -> None:
        self.prev_config_dir = os.environ.get("BANK2YNAB_CONFIG_DIR")

    def tearDown(self) -> None:
        if self.prev_config_dir is None:
            os.environ.pop("BANK2YNAB_CONFIG_DIR", None)
        else:
            os.environ["BANK2YNAB_CONFIG_DIR"] = self.prev_config_dir

    def test_packaged_defaults_are_copied_to_user_config_dir(self) -> None:
        with tempfile.TemporaryDirectory() as temp_config:
            os.environ["BANK2YNAB_CONFIG_DIR"] = temp_config

            handler = ConfigHandler()

            bank_conf = Path(temp_config) / "bank2ynab.conf"
            user_conf = Path(temp_config) / "user_configuration.conf"
            self.assertEqual(Path(handler.bank_conf_path), bank_conf)
            self.assertEqual(Path(handler.user_conf_path), user_conf)
            self.assertTrue(bank_conf.exists())
            self.assertTrue(user_conf.exists())


if __name__ == "__main__":
    unittest.main()
