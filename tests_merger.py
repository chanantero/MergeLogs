import unittest
import merger

class TestsMerger(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_merge_log_lines(self):
        # Given
        log_lines_1 = ['[20190628 11:00:00] blabla', '[20190628 12:00:00] blabla']
        log_lines_2 = ['[20190628 11:30:00] blabla, [20190628 12:00:01] blabla']
        expected_log_lines = ['[20190628 11:00:00] blabla', '[20190628 11:30:00] blabla', '[20190628 12:00:00] blabla', '[20190628 12:00:01] blabla']

        # When
        merged_log = merger.merge_logs_lines(log_lines_1, log_lines_2)

        # Then
        self.assertEqual(expected_log_lines, merged_log)

    def test_text_to_line_list(self):
        # Given
        txt = '[20190628 11:00:00] blabla\n[20190628 12:00:00] blabla'
        expected_list = ['[20190628 11:00:00] blabla', '[20190628 12:00:00] blabla']

        # When
        line_list = merger.text_to_line_list(txt)

        # Then
        self.assertEqual(expected_list, line_list)
