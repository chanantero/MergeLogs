import os
import unittest
import merger
import datetime

class TestsMerger(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_merge_logs(self):
        # Given
        txt_1 = '[20190628 11:00:00:000000] blabla\n[20190628 12:00:00:000000] blabla'
        txt_2 = '[20190628 11:00:00:100000] blabla\n[20190628 11:59:00:000000] blabla'
        expected_lines = ['[20190628 11:00:00:000000] blabla\n',
                          '[20190628 11:00:00:100000] blabla\n',
                          '[20190628 11:59:00:000000] blabla\n',
                          '[20190628 12:00:00:000000] blabla']
        file_object = open('test_file_1.txt', 'w')
        file_object.write(txt_1)
        file_object.close()
        file_object = open('test_file_2.txt', 'w')
        file_object.write(txt_2)
        file_object.close()

        # When
        merger.merge_logs('test_file_1.txt', 'test_file_2.txt', 'test_merge_logs.txt')

        # Then
        file_object = open('test_merge_logs.txt', 'r')
        lines = file_object.readlines()
        self.assertEqual(expected_lines, lines)
        file_object.close()

        # Finally
        os.remove("test_file_1.txt")
        os.remove("test_file_2.txt")
        os.remove("test_merge_logs.txt")

    def test_should_merge_log_lines(self):
        # Given
        line1 = '[20190701 07:57:34:108335] [1m[37m[Info]    [0m[0;34m[MME 1]->[eNB] Error Indication (unknown target id)[0m'
        line2 = '[20190701 07:57:34:108340] [1m[37m[Info]    [0m000f4009000001000240020160'
        line3 = '[20190701 07:58:38:874164] [1m[37m[Info]    [0mDL[1m[32m A[0m[   0][   0][1m[31m N[0m[   0][   0][1m[33m D[0m[   0][   0]  -  UL[1m[32m A[0m[   0][1m[31m N[0m[   0][1m[33m D[0m[   0] - 0 UEs - %CPU  9.84'
        line4 = '[20190701 07:58:39:874183] [1m[37m[Info]    [0mDL[1m[32m A[0m[   0][   0][1m[31m N[0m[   0][   0][1m[33m D[0m[   0][   0]  -  UL[1m[32m A[0m[   0][1m[31m N[0m[   0][1m[33m D[0m[   0] - 0 UEs - %CPU  9.72'
        log_lines_1 = [line1, 'no datetime', line3]
        log_lines_2 = [line2, line4]
        expected_log_lines = [line1, line2, line3, line4]

        # When
        merged_log = merger.merge_logs_lines(log_lines_1, log_lines_2)

        # Then
        self.assertEqual(expected_log_lines, merged_log)

    def test_get_date_time_from_log_line(self):
        # Given
        log_line = '[20190701 09:42:02:047427] [1m[37m[Info]    [0m[Cell] Synchronized with GPS'
        expected_date_time = datetime.datetime(2019, 6, 28, 11, 0, 0, 0)

        # When
        date_time = merger.line_date_time(log_line)

        # Then

    def test_dont_fail_when_there_is_no_date_time(self):
        # Given
        log_line = 'blabla'

        # When
        date_time = merger.line_date_time(log_line)

        # Then
        self.assertEqual(None, date_time)

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

        # Finally
        os.remove(txt_file)
