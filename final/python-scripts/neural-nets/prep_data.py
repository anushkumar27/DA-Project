'''l_mod = ','.join([f.strip() for f in l.strip().split(';')])
l_mod[0] = 0 if l_mod[0] == '"GP"' else 1
l_mod[1] = 0 if l_mod[1] == '"F"' else 1
l_mod[3] = 0 if l_mod[3] == '"U"' else 1
l_mod[4] = 0 if l_mod[4] == '"LE3"' else 1
l_mod[5] = 0 if l_mod[5] == '"T"' else 1
l_mod[8] = 0 if l_mod[8] == 'U' else 1
l_mod[9] = 0 if l_mod[9] == 'U' else 1
'''

'''
stu_file = open('student-mat.csv')
op_file = open('student-mat-proc.csv', mode='w')

header = ','.join([ f.strip() for f in stu_file.readline().strip().split(';')])

mappings = {

}

# need:
# famrel
# freetime
# goout
# Dalc
# Walc
# health
# absences
# G1
# G2
# G3
for l in stu_file:
        l_mod = ','.join([f.strip() for f in l.strip().split(';')])
        l_mod = []
'''

import csv

# famrel freetime goout Dalc Walc health absences G1 G2 G3
desired = [
	'famrel',
	'freetime',
	'goout',
	'Dalc',
	'Walc',
	'health',
	'absences',
	'G1',
	'G2',
	'G3'
]

f = open('student-mat.csv')
of = open('student-mat-mod-mod.csv', 'w', newline='')
r = csv.DictReader(f,delimiter=';')
w = csv.DictWriter(of, fieldnames=desired)
w.writeheader()

for line in r:
	m_line = {
	'famrel':None,
	'freetime':None,
	'goout':None,
	'Dalc':None,
	'Walc':None,
	'health':None,
	'absences':None,
	'G1':None,
	'G2':None,
	'G3':None
}
	for k in line.keys():
		if k in desired:
			m_line[k] = line[k]
	w.writerow(m_line)
