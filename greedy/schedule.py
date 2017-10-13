import sys
import re

def schedule_jobs(lst):
    lst.sort(key = lambda row: (row[0] - row[1], row[0]), reverse=True)

def find_weight(lst):
    totalweight = 0
    time = 0
    for row in lst:
        jobweight, joblength = row[0], row[1]
        time += joblength
        completiontime = jobweight * time
        totalweight += completiontime
    return totalweight


if __name__ == '__main__':
    joblist = []
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = re.findall(r'\d+',line)
            if len(line_lst) > 1:
                joblist.append([int(line_lst[0]), int(line_lst[1])])
    schedule_jobs(joblist)
    print(find_weight(joblist))
