from unittest import mock
from testing_base import get_display_output, set_keyboard_input,clearTables
import main

@mock.patch("home.importantlinks")
def test_importantLinks(importantlinks_mock):  #Display the new login space
    set_keyboard_input(["importantlinks", "10", "Exit"])
    main.main()
    importantlinks_mock.assert_called()

