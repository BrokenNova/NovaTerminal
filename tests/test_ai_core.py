import unittest
from src.ai_core import NovaAI

class TestNovaAI(unittest.TestCase):
    def test_respond(self):
        ai = NovaAI()
        self.assertEqual(ai.respond("test"), "Nova Terminal says: 'I'm here to assist with test'")

if __name__ == "__main__":
    unittest.main()
