import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.saldot = {1: 10, 2: 3}
        self.tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "piimä", 2),
        }
        self.varasto_mock = Mock()
        self.varasto_mock.saldo.side_effect = self.saldot.get
        self.varasto_mock.hae_tuote.side_effect = self.tuotteet.get

        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_maksettaessa_ostos_tilisiirto_kutsutaan_oikeilla_arugmenteilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)

    def test_ostaessa_kaksi_eri_tuotetta_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        self.viitegeneraattori_mock.uusi.return_value = 43

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 43, "12345", ANY, 7)

    def test_ostaessa_kaksi_samaa_tuotetta_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        self.viitegeneraattori_mock.uusi.return_value = 43

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 43, "12345", ANY, 10)

    def test_ostaessa_yksi_tuote_ja_toinen_loppunut_tuote_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        self.viitegeneraattori_mock.uusi.return_value = 43
        self.saldot[2] = 0

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 43, "12345", ANY, 5)
