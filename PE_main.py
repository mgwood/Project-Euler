import time,PE11,PE13,PE14,PE16,PE17,PE18,PE19,PE20,PE21,PE40

f = open('pe_main_results.txt', 'w')

#currently the PE_solutions.txt file has solutions for problems 1-50 in order
solutions = open('PE_solutions.txt','r')
solution_list =[]

while True:
    line = solutions.readline()
    if len(line)==0:
        break
    else:
        solution_list.append(int(line))

correct_results = 0
total_results = 0
incorrect_results = []

run_time = [time.time()]
exercises = []

for key in globals().keys():
    if 'PE' in key:
        exercises.append(key[2:])

for ii in exercises:
    #getattr() call is used to programatically call the main() method for each
    #PEX.py where X is both imported and in the exercises array
    if getattr(globals()['PE'+ii],'main')() == solution_list[int(ii)-1]:
        f.write('PE'+ii+': Success!\n')
        if len(run_time)==1:
            run_time.append(time.time()-(run_time[-1]))
        else:
            run_time.append(time.time()-(run_time[-1]+run_time[0]))
        f.write('Time: ' + str(run_time[-1])+'\n')
        f.write('\n')
        correct_results+=1
        total_results+=1
    else:
        f.write('PE'+str(ii)+': Failure!\n')
        if len(run_time)==1:
            run_time.append(time.time()-(run_time[-1]))
        else:
            run_time.append(time.time()-(run_time[-1]+run_time[0]))

        f.write('Time: ' + str(run_time[-1])+'\n')
        f.write('\n')
        total_results+=1
        incorrect_results.append(ii)

run_time.pop(0)

print 'Execution complete!'
f.write('Execution complete:'+'\n')
f.write('Exercises attempted: '+str(total_results)+'\n')
f.write('Exercises correct: '+str(correct_results)+'\n')
f.write('\n')
f.write('Percent complete: '+str(100.0*correct_results/total_results)+'%'+'\n')

if len(incorrect_results)>0:
    f.write('Incorrect exercies:'+'\n')
    f.write(str(incorrect_results))

sub_minute_count = 0

for s_time in run_time:
    if s_time<60:
        sub_minute_count+=1

def max_runtime(run_times,exercises):
    m = max(run_times)
    for ele in range(len(run_times)):
        if run_times[ele]==m:
            return str(exercises[ele])

if sub_minute_count==total_results:
    f.write('All solutions completed in less than 1 minute.\n')
else:
    f.write(str(sub_minute_count)+' solutions in less than 1 minute.\n')

f.write('Longest solution time: '+str(max(run_time))+' for problem '+max_runtime(run_time,exercises))
f.write('\n')
f.write('\n')

f.close()

