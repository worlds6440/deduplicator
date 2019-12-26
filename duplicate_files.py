import os
import zlib


def find_files(url, ext_list):
    result = []
    ext = [x.lower() for x in ext_list]
    for root, dirs, files in os.walk(url):
        for file in files:
            # if file.endswith(ext):
            if file.split('.')[-1].lower() in ext:
                result.append(os.path.join(root, file))
    return result


def crc(a_file_name):
    prev = 0
    for eachLine in open(a_file_name, "rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X" % (prev & 0xFFFFFFFF)


def add_files_to_crc_dict(result_dict, file_list):
    ''' Add to the dictionary a list of files that match
        the CRC value. If not already in dictionary, add it.

        dict(){
            [CRC:FILESIZE] : (file1.xyz, file2.xyz...)
            [CRC:FILESIZE] : (file1.xyz, file2.xyz...)
        }
    '''
    for x in file_list:
        dict_index = "{}:{}".format(crc(x), os.path.getsize(x))
        try:
            number_of_dups = len(result_dict[dict_index])
            if number_of_dups == 0:
                print("found zero dups")
            else:
                result_dict[dict_index].append(x)
        except:
            result_dict[dict_index] = [x]
    return result_dict


# Find all files in folder with file extension
filename1 = "D:\\Google Drive"
filename2 = "D:\\Google Photos"
result1 = find_files(filename1, ["jpg", "jpeg", "png"])
result2 = find_files(filename2, ["jpg", "jpeg", "png"])

# Create CRC value for each file and add
# it to the dictionary of combined files
result_dict = dict()
result_dict = add_files_to_crc_dict(result_dict, result1)
result_dict = add_files_to_crc_dict(result_dict, result2)

# Find duplicates
duplcate_filesize = 0
for key in result_dict:
    num_files = len(result_dict[key])
    if num_files > 1:
        # Duplicate found
        filesize = int(key.split(':')[-1])
        duplcate_filesize += (filesize * (num_files - 1))
        print(key, result_dict[key])
        # os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

# report how much diskspace will be saved
print("{}MB".format((duplcate_filesize/1024)/1024))
