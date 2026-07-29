import unittest
import telefonbuch_logik_1a

class TestText(unittest.TestCase):

    def test_pruefe_text(self):
        self.assertEqual(telefonbuch_logik_1a.pruefe_text("sadasde212312gsdfäppÜÜÜ"), True)
        self.assertEqual(telefonbuch_logik_1a.pruefe_text("max_mustermann@google.de"), False)


    def test_pruefe_nummer(self):
        self.assertEqual(telefonbuch_logik_1a.pruefe_nummer("213123123 / 123"), True)
        self.assertEqual(telefonbuch_logik_1a.pruefe_nummer("asd / 123"), False)



if __name__ == "__main__":
    unittest.main()