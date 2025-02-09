import unittest
from unittest.mock import patch, MagicMock
from main import main


class TestMain(unittest.TestCase):
    @patch("builtins.input", return_value="Alice")
    @patch("builtins.print")
    def test_main_output(self, mock_print: MagicMock, mock_input: MagicMock) -> None:
        main()
        mock_input.assert_called_once_with("Please enter your name: ")
        mock_print.assert_called_once_with("Hello, Alice!")


if __name__ == "__main__":
    unittest.main()
