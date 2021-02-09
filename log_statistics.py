import os, collections
files_path = r"c:\temp\Logs"
files = [f for f in os.listdir(files_path) if os.path.isfile(os.path.join(files_path, f))]
source_ip_set = set()
for file in files:
    with open(os.path.join(files_path, file), 'r') as f:
        lines = f.readlines()
        case, case_ip, source_ip_dict = 0, "", collections.defaultdict(int)
        print(f"{file} has {len(lines)} log lines")
        for line in lines:
            if line[0].isdigit():
                source_ip = line.split(" ")[2].strip()
                if case_ip != source_ip:
                    case_ip = source_ip
                    case += 1
                    source_ip_dict[source_ip] += 1
                    source_ip_set.add(source_ip)

        print(f'{file} has {case} total cases')
        print(f'{file} has cases by source_ip as {source_ip_dict}')
print(f'The source IP set is {source_ip_set}')