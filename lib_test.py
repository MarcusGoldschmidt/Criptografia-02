import unittest
import lib


class TestGenerateMethods(unittest.TestCase):

    def test_generate_block(self):
        key = 'IC'

        text = 'ADA'

        assert_blocks = [
            '0100000101000100',
            '0100000100000000'
        ]

        key_bits = lib.text_to_bits(key)
        file_bits = lib.text_to_bits(text)

        self.assertEqual(lib.complete_blocks(key_bits, file_bits), assert_blocks)

    def test_generate_encrypt(self):
        key = 'IC'

        text = 'ADA'

        assert_test = '00001000000001110000100001000011'

        mode = lib.Mode.CRIPTO

        self.assertEqual(lib.process(key, text, mode), assert_test)

    def test_xor_basic(self):
        key = '101010011'

        text = '101010011'

        assert_test = '000000000'

        self.assertEqual(lib.make_xor(key, text), assert_test)


unittest.main()
