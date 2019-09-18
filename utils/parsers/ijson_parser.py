import ijson
#FILE_NAME = 'tej.json'
FILE_NAME = 'small_data.json'

with open(FILE_NAME, 'r') as f_ptr:
    parser = ijson.parse(f_ptr)
    for prefix, event, value in parser:
        print(prefix)
        print(event)
        print(value)
        print('')
