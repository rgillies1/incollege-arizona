from unittest import mock
from testing_base import get_display_output, set_keyboard_input, clearTables
import main


#checks if return to main after going to the important link page
@mock.patch("home.importantLinks")
def test_importantLinks(importantlinks_mock):  #Display the new login space
    set_keyboard_input(["ImportantLinks", "10", "Exit"])
    main.main()
    importantlinks_mock.assert_called()


#test useful links
@mock.patch("home.usefulLinks")
def test_usefulLinks(usefulLinks_mock):
    set_keyboard_input(["UsefulLinks", "10", "Exit"])
    main.main()
    usefulLinks_mock.assert_called()


@mock.patch("importantLinks.GuestControls")
def test_Guest_Controls(GuestControls_mock):
    set_keyboard_input(["ImportantLinks", "5", "0", "4", "10", "Exit"])
    main.main()
    GuestControls_mock.assert_called()

#need to fix this 
@mock.patch("importantLinks.changelanguage")
def test_changelanguage(changelanguage_mock):
    set_keyboard_input(["\nLogin", "Dominos", "Dominos@2", "8", "9", "1", "Exit", "Exit"])
    main.main()
    changelanguage_mock.assert_called()