import unittest
from password_validator import *


class TestValidator(unittest.TestCase):

    def test_password_min_length(self):
        text = "hi"
        assert not check_valid_length(text)

    def test_password_enough_length(self):
        text = "12345678"
        assert check_valid_length(text)

    def test_password_max_length(self):
        text = "teeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeds;'gkljmsdfgkmdfgl;knmdfgkl;dfmgldfkgd" \
               "fklgmdfgkmdfkl;mdfklgmdfklgmfldkgmlfkdgmfldkgmfdl;kgmsdl;mgfdlkgdfklgmf;klgmldkfsgl;kdmfglkdfgkldfgdfl" \
               "kdflkfkg;kldfgsdfklmsdlfkgsdfl;gmsdflkmsdflkmdfklmd;flgfkl;mfdklgdflkdkl;gdkl;gdlfkgmsldkfgsdklmsl;dg" \
               ";lkdmg;dfkmg;kldgmk;flmgkldmgkl;fmgkldmgdfklg;klgmdlkgldfkdfklgdfklg;fklmglfkdgl;dfm"
        assert not check_valid_length(text)

    def test_password_ascii_chars(self):
        text = "öööööööööö"
        assert not check_valid_ascii_chars(text)

    def test_password_if_weak(self):
        text = "password"
        assert not check_if_not_a_weak_pw(text, {"1234", "password"})

    def test_not_weak_password_if_weak(self):
        text = "the_most_random_password_in_the_world_123"
        assert check_if_not_a_weak_pw(text, {"Hello", "World"})

    def test_password_non_printable(self):
        text = "àáâ"
        assert replace_non_printable(text, '*') == '***'

    def test_password_non_printable_in_ascii(self):
        text = "qwerty123"
        assert replace_non_printable(text, '*') == 'qwerty123'


if __name__ == '__main__':
    unittest.main()
