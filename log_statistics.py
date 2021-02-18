import os
import collections
import pandas as pd
files_path = r"c:\temp\Logs"
files = [f for f in os.listdir(files_path) if os.path.isfile(os.path.join(files_path, f)) and f.split('.')[-1] == 'log']
ip_pd = pd.DataFrame()
for file in files:
    with open(os.path.join(files_path, file), 'r') as f:
        lines = f.readlines()
        case, source_ip_dict = 0, collections.defaultdict(int)
        print(f"{file} has {len(lines)} log lines")
        for line in lines:
            if ' MAIL ' in line:
                source_ip = line.split(" ")[2].strip()
                case += 1
                source_ip_dict[source_ip] += 1

        print(f'{file} has {case} total cases')
        print(f'{file} has cases by source_ip as {source_ip_dict}')
        ip_pd = ip_pd.append(pd.DataFrame(source_ip_dict, index=[file]))
ip_pd.to_csv(os.path.join(files_path, "out.csv"), index=True, header=True)