import os
import time
import xml.etree.cElementTree as ET


def get_file_size_in_mb(file_name):
    """
    Method to check the file size in MB
    """
    file_size = 0
    if os.path.isfile(file_name):
        file_size = os.path.getsize(file_name)
        file_size = round(file_size / (1024 * 1024.0), 2)
    file_size = '{:,.2f}'.format(file_size)
    return str(file_size) + ' MB'


def read_xml_file(xml_file, element):
    """
    Parse the xml file to xml.etree.cElementTree
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    number_of_element = len(root.findall(element))
    return '{:,.0f}'.format(number_of_element)


if __name__ == '__main__':
    xml_file_name = 'large_xml_file.xml'
    print(f'File Size: {get_file_size_in_mb(xml_file_name)}')
    start_time = time.perf_counter()
    counter = read_xml_file(xml_file_name, 'ProteinEntry/header')
    end_time = time.perf_counter()
    total_time = round(end_time - start_time, 2)
    print(f'Total time taken:[{total_time}] seconds to identify the number of elements: [{counter}]')
