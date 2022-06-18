import unittest
# sys.path.append(os.path.abspath(os.path.join('..')))
from application.models import User

class TestModels(unittest.TestCase):
    

    def setUp(self):
        self.mnemonic_phrase = "clump capable north later panic main rely repeat undo extra say engage scatter total update little appear alley actual sting piano other copper able pool"
        self.user = User(self.mnemonic_phrase)


    def test_id(self):
        sk = "YnmILNXXTxmutrZnR9R/pTRgl9OdglSgwQVeDVJ0/kXRKPEFL37lwcMel0Vl6pCOc292Wl+jy8gGsKsg3VVokw=="
        self.assertEqual(self.user.id(), sk)


    def test_public_key(self):
        pk = "2EUPCBJPP3S4DQY6S5CWL2UQRZZW65S2L6R4XSAGWCVSBXKVNCJ3OA22P4"
        self.assertEqual(self.user.id(), pk)

    

if __name__ == '__main__':
    unittest.main()

