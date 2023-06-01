file_name1 = '1.txt'
file_name2 = '2.txt'
file_name3 = '3.txt'
output_file = 'output.txt'
file_list = []
with open (file_name1, 'r', encoding='utf-8') as file1, open (file_name2, 'r', encoding='utf-8') as file2, open (file_name3, 'r', encoding='utf-8') as file3:
    s1 = file1.readlines()
    s2 = file2.readlines()
    s3 = file3.readlines()
    file_list = [[len(s1), file_name1, s1], [len(s2), file_name2, s2], [len(s3), file_name3, s3]]
    file_list.sort()
    #print(file_list)
with open (output_file, 'w', encoding='utf-8') as output:
    for f in file_list:
        output.write(f[1]+'\n')
        output.write(str(f[0])+'\n')
        output.writelines(f[2])
        output.write('\n')