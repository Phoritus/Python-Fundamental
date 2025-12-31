import sys
from unittest.mock import MagicMock

# Create mock logging_setup module
mock_logging_setup = MagicMock()
mock_logging_setup.setup_logging = MagicMock(return_value=MagicMock())

# Add mock to sys.modules
sys.modules['logging_setup'] = mock_logging_setup