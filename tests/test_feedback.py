import builtins
from unittest.mock import patch
from app.main import get_feedback

def test_get_feedback():
    with patch('builtins.input', return_value='Great app!'):
        with patch('builtins.print') as mocked_print:
            feedback = get_feedback()
            mocked_print.assert_called_with("Feedback submitted: Great app!")
            assert feedback == 'Great app!'
