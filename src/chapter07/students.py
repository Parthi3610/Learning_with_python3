students = [
    ('parthi', ['math', 'science', 'english']),
    ('gopi', ['hindi', 'tamil', 'math']),
    ('smruthi', ['math', 'electronics']),
    ('kanwar', ['english', 'hindi', 'social']),
    ('jay', ['math', 'social', 'electronics'])]

count = 0

for (name,subjects) in students:
    # print(name, len(subjects))
    for subject in subjects:
        if subject == 'math':
            count += 1

print ("number of people taking math: ", count)



