import re
import datetime

def line_date_time(line):
    m = re.search(r'\[(.*\d+.*)\]', line)
    date_time_string = m.group(1)
    date_time = datetime.datetime.strptime(date_time_string,"%y%m%d %H:%M:%S:%f")
    return date_time


def merge_logs_lines(log_lines_1, log_lines_2):

    date_time_1 = []
    for line in log1_lines:
        date_time_1.append(line_date_time(line))

    date_time_2 = []
    for line in log2_lines:
        date_time_2.append(line_date_time(line))

    merged_log = 'hola'
    return merged_log
