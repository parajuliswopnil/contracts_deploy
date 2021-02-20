from ..my_testnet_score import TestnetScore
from tbears.libs.scoretest.score_test_case import ScoreTestCase


class TestTestnetScore(ScoreTestCase):

    def setUp(self):
        super().setUp()
        self.score = self.get_score_instance(TestnetScore, self.test_account1)

    def test_hello(self):
        self.assertEqual(self.score.hello(), "Hello")
