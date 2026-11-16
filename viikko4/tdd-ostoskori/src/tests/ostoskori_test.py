import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_oikea_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)


    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        piima = Tuote("Piimä", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(piima)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)


    def test_kahden_tuotteen_lisaamisen_jalkeen_oikea_hinta(self):
        maito = Tuote("Maito", 3)
        piima = Tuote("Piimä", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(piima)

        self.assertEqual(self.kori.hinta(), 4)

    def test_ostokset_palauttaa_listan_jossa_yksi_tuote(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_lisatyn_tuotteen_ostos_nimi_ja_lukumaara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), maito.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        piima = Tuote("Piimä", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(piima)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)
