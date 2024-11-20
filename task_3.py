file_list = ['1.txt','2.txt','3.txt']

files_content = {}
files_len = {}

for file in file_list:
    with open(file, encoding="utf-8") as f:
        lines_list = f.readlines()
        files_content[file] = lines_list
        files_len[file] = len(lines_list)

sorted_files = sorted(files_len.items(), key=lambda item: item[1])

with open('result_file.txt', "w", encoding="utf-8") as r:
    for file,cnt in sorted_files:
        r.write(file+"\n")
        r.write(str(cnt)+"\n")
        r.write("".join(files_content[file]))
        r.write("\n")

