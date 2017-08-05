# -*- coding: utf-8 -*-

import datetime
import os

class DatetimeUtil:
    @staticmethod
    def dt_to_dow(dt_obj, dows):
        w = dt.weekday()
        return dows[w]

def list2file(filepath, ls):
    with open(filepath, 'w') as f:
        f.writelines(['%s\n' % line for line in ls] )

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='A plain list calender generator.'
    )
    parser.add_argument('-y', '--year', type=int,
        default=datetime.date.today().year,
        help='A year you want to generate.')

    parsed_args = parser.parse_args()
    return parsed_args

args = parse_arguments()

SELF_DIR = os.path.abspath(os.path.dirname(__file__))
start_year = start_year = args.year

#  ---- [ Customization Area ----
format_filename = '%d.md'
format_section  = '# %Y/%m'
format_line     = '- %y%m%d'
dows            = ['mon','tue','wed','thu','fri','sat','SUN']
#  ---- Customization Area ] ----

lines = []
y = start_year
m = 1
d = 1
today = datetime.date.today()
dt = datetime.date(y, m, d)
day_adder = datetime.timedelta(days=1)

while True:
    if dt.day==1:
        lines.append(dt.strftime(format_section))

    dow = DatetimeUtil.dt_to_dow(dt, dows)
    line = '%(date)s %(dow)s ' % {
        'date' : dt.strftime(format_line),
        'dow'  : dow
    }
    lines.append(line)

    dt += day_adder
    if dt.year != y:
        break

if len(lines)!=0:
    fullpath = os.path.join(SELF_DIR, format_filename % y)
    list2file(fullpath, lines)
