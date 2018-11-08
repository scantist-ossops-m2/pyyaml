import yaml
import pprint
import sys

def test_sort_keys(input_filename, sorted_filename, verbose=False):
    input = open(input_filename, 'rb').read().decode('utf-8')
    sorted = open(sorted_filename, 'rb').read().decode('utf-8')
    data = yaml.load(input)
    dump_sorted = yaml.dump(data, default_flow_style=False, sort_keys=True)
    dump_unsorted = yaml.dump(data, default_flow_style=False, sort_keys=False)
    dump_unsorted_safe = yaml.dump(data, default_flow_style=False, sort_keys=False, Dumper=SafeDumper)
    if verbose:
        print("INPUT:")
        print(input)
        print("DATA:")
        print(data)

    assert dump_sorted == sorted

    if sys.version_info>=(3,7):
        assert dump_unsorted == input
        assert dump_unsorted_safe == input

test_sort_keys.unittest = ['.sort', '.sorted']

if __name__ == '__main__':
    import test_appliance
    test_appliance.run(globals())

