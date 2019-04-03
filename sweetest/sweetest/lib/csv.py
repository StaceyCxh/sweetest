import csv


def read_csv(csv_file, encoding=None):
    '''
    读取csv文件中的数据
    :param csv_file: csv文件
    :param encoding: 编码方式
    :return: csv文件中的数据
    '''
    data = []
    with open(csv_file, encoding=encoding, errors='ignore') as f:
        reader = csv.reader(f)
        for line in reader:
            data.append(line)
    return data


def write_csv(csv_file, data, encoding=None):
    '''
    将数据写入csv文件
    :param csv_file: csv文件
    :param data: 数据
    :param encoding: 编码方式
    '''
    with open(csv_file, 'w', encoding=encoding, newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
