#!/usr/bin/env python

import csv

def gender_correlation():
    defaults = 0
    men = 0
    women = 0
    f = open('training_set.csv', 'rb')
    a = 0
    reader = csv.reader(f)
    for row in reader:
        if a <= 1:
            a += 1
        else:
            val = int(row[24])
            if int(row[2]) == 1:
                men += val
                defaults += val
            else:
                women += val
                defaults += val
           # print "Gender is " + str(row[2]) + " and default: " + str(row[24])
    print "Men: " + str(men)
    print "Women: " + str(women)
    print "Total Defaults: " + str(defaults)
    f.close()

def education_correlation():
    e = {}
    e['total_defaults'] = 0
    e['total_grads'] = 0
    e['total_college'] = 0
    e['total_high'] = 0
    e['total_other'] = 0
    e['grad_defaults'] = 0
    e['college_defaults'] = 0
    e['high_defaults'] = 0
    e['other_defaults'] = 0
    f = open('training_set.csv', 'rb')
    a = 0
    reader = csv.reader(f)
    for row in reader:
        if a <= 1:
            a += 1
        else:
            val = int(row[24])
            check = int(row[3])
            if check == 1:
                e['grad_defaults'] += val
                e['total_grads'] += 1
                e['total_defaults'] += val
            elif check == 2:
                e['college_defaults'] += val
                e['total_college'] += 1
                e['total_defaults'] += val
            elif check == 3:
                e['high_defaults'] += val
                e['total_high'] += 1
                e['total_defaults'] += val
            elif check == 4:
                e['other_defaults'] += val
                e['total_other'] += 1
                e['total_defaults'] += val
            else:
                e['total_defaults'] += val
    print "Total Grads: " + str(e['total_grads'])
    print "Grad Defaults: "  + str(e['grad_defaults'])
    print "Total Undergrads: " + str(e['total_college'])
    print "Undergrad Defaults: " + str(e['college_defaults'])
    print "Total High School: " + str(e['total_high'])
    print "High School Defaults: " + str(e['high_defaults'])
    print "Total Other: " + str(e['total_other'])
    print "Other Defaults: " + str(e['other_defaults'])
    print "Total Defaults " + str(e['total_defaults'])
    f.close()
    
gender_correlation()
education_correlation()
