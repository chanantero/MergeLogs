import re
import datetime

def merge_logs(log_file_1, log_file_2, merged_log_file_name, prefix_1=None, prefix_2=None):
    log_lines_1 = file_to_line_list(log_file_1)
    log_lines_2 = file_to_line_list(log_file_2)
    merged_log = merge_logs_lines(log_lines_1, log_lines_2, prefix_1, prefix_2)
    file_object = open(merged_log_file_name, 'w')
    file_object.write("\n".join(merged_log))
    file_object.close()

def merge_logs_lines(log_lines_1, log_lines_2, prefix_1=None, prefix_2=None):

    date_time_1 = []
    inds_1 = []
    count = 0
    for line in log_lines_1:
        date_time = line_date_time(line)
        if date_time is not None:
            inds_1.append(count)
            date_time_1.append(date_time)
        count = count + 1

    date_time_2 = []
    inds_2 = []
    count = 0
    for line in log_lines_2:
        date_time = line_date_time(line)
        if date_time is not None:
            inds_2.append(count)
            date_time_2.append(date_time)
        count = count + 1

    sorted_info = sort_date_time_lists(date_time_1, date_time_2)

    merged_log = []
    for i in range(0, sorted_info['num_elements']):
        if sorted_info['groups'][i] == 0:
            if prefix_1 is not None:
                merged_log.append(prefix_1+log_lines_1[inds_1[sorted_info['indices'][i]]])
            else:
                merged_log.append(log_lines_1[inds_1[sorted_info['indices'][i]]])
        elif sorted_info['groups'][i] == 1:
            if prefix_1 is not None:
                merged_log.append(prefix_2+log_lines_2[inds_2[sorted_info['indices'][i]]])
            else:
                merged_log.append(log_lines_2[inds_2[sorted_info['indices'][i]]])

    return merged_log


def sort_date_time_lists(date_time_1, date_time_2):
    date_times = date_time_1 + date_time_2
    date_times_original = list(date_times)
    ind_1 = list(range(0, len(date_time_1)))
    ind_2 = list(range(0, len(date_time_2)))
    inds_original = ind_1 + ind_2
    group_1 = [0]*len(ind_1)
    group_2 = [1]*len(ind_2)
    groups_original = group_1 + group_2
    date_times.sort()

    indices = []
    groups = []
    for date_time in date_times:
        i = date_times_original.index(date_time)
        indices.append(inds_original[i])
        groups.append(groups_original[i])

    return {'num_elements': len(date_times), 'indices': indices, 'groups': groups}


def line_date_time(line):
    m = re.search(r'\[([\d|\s|:]+)\]', line)
    if m is not None:
        date_time_string = m.group(1)
        date_time = datetime.datetime.strptime(date_time_string,"%Y%m%d %H:%M:%S:%f")
        return date_time
    else:
        return None 


def file_to_line_list(file_name):
    file_object = open(file_name, 'r')
    lines = file_object.readlines()
    lines = [x.strip() for x in lines]
    return lines
