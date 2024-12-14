from app.features import DarkMode

def test_dark_mode_toggle():
    dark_mode = DarkMode()
    assert dark_mode.toggle() == True  # Toggle on
    assert dark_mode.toggle() == False  # Toggle off
