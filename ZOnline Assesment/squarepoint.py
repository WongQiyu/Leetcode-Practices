from io import StringIO

txt = '''1 ,Alan,Chef,40000,2018-10-29,,
2 ,Brenda,Teacher,30000,,2018-01-13,
3 ,Charlie,CEO,1000000,2015-09-27,,
4 ,Declan,Head of Sales,200000,2018-05-28,,
5 ,Erin, Taxi Driver, 35000,2018-09-21,,
6 ,Frank,Taxi Driver, 35000,016-08-03,,
7 ,Gertrude,Head Chef,45000,2013-12-11,2016-11-29
8 ,Harry,,60000,2012-09-14,2013-09-17
9 ,Isabella,Police Officer,33000,2014-03-21,2014-09-24
10,John,Data Scientist,45000,2015-07-15,2019-04-28
11,Kerry,Shop Keeper, 22000,2017-04-03,,
12,Liam,Chef,40000,2012-06-13,2015-02-18
13,Mandy,Gardener,80000,2018-01-26,,
14,Nigel,Teacher,30000,2015-01-01,,
15,Ophelia,Clergy,55000,2015-04-04,2019-01-24
16,Peter,Chef,40000,2020-01-03,,
17,Quinn,Unemployed,0,2016-02-25,2019-07-04
18,Roger,Martial Arts Teacher,27500,2016-05-03,2018-09-17
19,Samantha,Teacher,,2015-06-29,,
20,Terry,Audio Engineer, 77000,2015-05-01,2015-08-02
21,, Pet Control,42000,2012-09-16,2014-11-06
22,Vanessa,Sous Chef,42000,2018-02-02,,
23,Willhelm,Business Owner,10000,2012-04-12,2014-06-25
24,Xavier,Teacher,30000,2018-02-07,2018-05-26
25,Yolanda,Taxi Driver, 35000,2017-12-17,2018-12-09
26,Zell,Chef,40000,2012-06-29,2013-04-02
14,Nigel,Teacher,30000,2015-01-01,,
15,Ophelia,Clergy,55000,2015-04-04,2019-01-24
16,Peter,Chef,40000,2020-01-03,,
25,Yolanda,Taxi Driver, 35000,2017-12-17,2018-12-09
26,Zell,Chef,40000,2012-06-29,2013-04-02'''

# Columns: employee_id,employee_name,job_title,salary,job_start_date,job_end_date
# Types: int,str,str,int,datetime,datetime
from datetime import datetime

def parse_file_other(iostring):
    # can try this way to readline rather than convoluted way below
    m_1 = StringIO(iostring)

    return [line.strip().split(',') for line in m_1.readlines()]




def parse_file(iostring):
    res = []
    m_1 = StringIO(iostring)
    #print([line.strip().split(',') for line in m_1.readlines()])
    #.readline
    for line in m_1:
        line = line.split(',')
        if line[-1] == '\n':
            line = line[:-1]
        line[3] = int(line[3]) if line[3] != '' else 0
        date_format = '%Y-%m-%d'
        print(line[4])
        try:
            date1 = datetime.strptime(datetime.today().strftime('%Y-%m-%d') ,date_format) if line[4] == '' else datetime.strptime(line[4], date_format)
        except ValueError:
            date1 = datetime.strptime(datetime.today().strftime('%Y-%m-%d') ,date_format)
        try:
            date2 = datetime.strptime(datetime.today().strftime('%Y-%m-%d') ,date_format) if line[5] == '' else datetime.strptime(line[5], date_format)
        except ValueError:
            date2 = datetime.strptime(datetime.today().strftime('%Y-%m-%d'), date_format)

        #line.append(line[5] - line[4])
        res.append(line)
    return res



def earned_more_than_30K(data_struct):
    res = [i for i in data_struct if i[3] and int(i[3]) > 30000]
    return len(res)

def held_job_longest_in_day(data_struct):
    ans = []
    date_format = '%Y-%m-%d'
    for line in data_struct:
        try:
            start = datetime.strptime(datetime.today().strftime('%Y-%m-%d'), date_format) if line[4] == '' else datetime.strptime(line[4], date_format)
        except ValueError:
            start = datetime.strptime('2' + line[4], date_format)
        end = datetime.strptime(datetime.today().strftime('%Y-%m-%d'), date_format) if line[5] == '' else datetime.strptime(line[5], date_format)
        ans.append((line[1],(end-start).days))
    longest = max(ans, key=lambda x:x[1])[1]
    print(longest)
    return [x[0] for x in ans if x[1] == longest ]

def second_highest_salary(data_struct):
    second_max = sorted(list(set([i[3] for i in data_struct])))[1]
    res = [i[1] for i in data_struct if i[3] == second_max]
    return " ".join(res)

# FileType: employee-salary
# Columns: employee_id,employee_name,job_title,salary,job_start_date,job_end_date
# Types: int,str,str,int,datetime,datetime

a = parse_file_other(txt)
print(a)
print(earned_more_than_30K(a))
print(second_highest_salary(a))
print(held_job_longest_in_day(a))