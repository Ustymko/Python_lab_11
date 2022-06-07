import re

logs_file = open("access.log.txt", "r")
logs_list = logs_file.read().split("\n")

# These logs are in time gap between 03:59:10 22/Mar/2009 and 08:13:32 25/Mar/2009
regex_for_unsuccessful_requests_logs = re.compile(".*(\\[22/Mar/2009:(03:59:[1-5][0-9]|0[4-9]:[0-5][0-9]:[0-5][0-9]|"
                                                  "1[0-9]:[0-5][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]:[0-5][0-9])|"
                                                  "\\[2[3-4]/Mar/2009:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]|"
                                                  "\\[25/Mar/2009:(0[0-7]:[0-5][0-9]:[0-5][0-9]|08:([0-1][0-2]:[0-5]"
                                                  "[0-9]|13:([0-2][0-9]|3[0-2])))).*(GET|POST).*\"\\s[4-5]\\d{2}.*")

logs_found = 0
for i in range(len(logs_list)):
    a = re.match(regex_for_unsuccessful_requests_logs, logs_list[i])
    if a:
        print(a.group())
        logs_found += 1

print(logs_found)
