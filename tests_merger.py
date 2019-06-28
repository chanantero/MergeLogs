import unittest
import merger
import datetime

class TestsMerger(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_merge_log_lines(self):
        # Given
        log_lines_1 = ['[20190628 11:00:00:000000] blabla', '[20190628 12:00:00:000000] blabla']
        log_lines_2 = ['[20190628 11:30:00:000000] blabla, [20190628 12:00:01:000000] blabla']
        expected_log_lines = ['[20190628 11:00:00:000000] blabla', '[20190628 11:30:00:000000] blabla', '[20190628 12:00:00:000000] blabla', '[20190628 12:00:01:000000] blabla']

        # When
        merged_log = merger.merge_logs_lines(log_lines_1, log_lines_2)

        # Then
        self.assertEqual(expected_log_lines, merged_log)

    def test_get_date_time_from_log_line(self):
        # Given
        log_line = '[20190628 11:00:00:000000] blabla'
        expected_date_time = datetime.datetime(2019, 6, 28, 11, 0, 0, 0)

        # When
        date_time = merger.line_date_time(log_line)

        # Then
        self.assertEqual(expected_date_time, date_time)

    def test_text_file_to_line_list(self):
        # Given
        txt = '[20190628 11:00:00:000000] blabla\n[20190628 12:00:00:000000] blabla'
        txt_file = 'test_file.txt'
        file_object = open(txt_file, 'w')
        file_object.write(txt)
        file_object.close()
        expected_list = ['[20190628 11:00:00:000000] blabla', '[20190628 12:00:00:000000] blabla']

        # When
        line_list = merger.file_to_line_list(txt_file)

        # Then
        self.assertEqual(expected_list, line_list)
