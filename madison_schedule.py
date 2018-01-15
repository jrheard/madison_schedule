import datetime


NORMAL = 'normal'
WEIRD = 'weird'
FLEX = 'flex'


raw_schedule = [
    {'date': '1/16/18', 'schedule': NORMAL},
    {'date': '1/18/18', 'schedule': NORMAL},
    {'date': '1/22/18', 'schedule': NORMAL},
    {'date': '1/24/18', 'schedule': WEIRD},
    {'date': '1/26/18', 'schedule': WEIRD},
    {'date': '1/31/18', 'schedule': NORMAL},

    {'date': '2/2/18', 'schedule': NORMAL},
    {'date': '2/6/18', 'schedule': NORMAL},
    {'date': '2/8/18', 'schedule': FLEX},
    {'date': '2/12/18', 'schedule': NORMAL},
    {'date': '2/14/18', 'schedule': FLEX},
    {'date': '2/16/18', 'schedule': NORMAL},
    {'date': '2/21/18', 'schedule': WEIRD},
    {'date': '2/23/18', 'schedule': NORMAL},
    {'date': '2/27/18', 'schedule': WEIRD},

    {'date': '3/1/18', 'schedule': FLEX},
    {'date': '3/5/18', 'schedule': NORMAL},
    {'date': '3/7/18', 'schedule': FLEX},
    {'date': '3/9/18', 'schedule': NORMAL},
    {'date': '3/13/18', 'schedule': NORMAL},
    {'date': '3/15/18', 'schedule': FLEX},
    {'date': '3/19/18', 'schedule': NORMAL},
    {'date': '3/21/18', 'schedule': FLEX},
    {'date': '3/23/18', 'schedule': NORMAL},

    {'date': '4/3/18', 'schedule': NORMAL},
    {'date': '4/5/18', 'schedule': FLEX},
    {'date': '4/9/18', 'schedule': NORMAL},
    {'date': '4/11/18', 'schedule': NORMAL},
    {'date': '4/16/18', 'schedule': NORMAL},
    {'date': '4/18/18', 'schedule': FLEX},
    {'date': '4/20/18', 'schedule': NORMAL},
    {'date': '4/24/18', 'schedule': NORMAL},
    {'date': '4/26/18', 'schedule': FLEX},
    {'date': '4/30/18', 'schedule': NORMAL},

    {'date': '5/2/18', 'schedule': FLEX},
    {'date': '5/4/18', 'schedule': NORMAL},
    {'date': '5/8/18', 'schedule': NORMAL},
    {'date': '5/10/18', 'schedule': FLEX},
    {'date': '5/14/18', 'schedule': NORMAL},
    {'date': '5/16/18', 'schedule': FLEX},
    {'date': '5/18/18', 'schedule': NORMAL},
    {'date': '5/22/18', 'schedule': NORMAL},
    {'date': '5/24/18', 'schedule': FLEX},
    {'date': '5/29/18', 'schedule': NORMAL},
    {'date': '5/31/18', 'schedule': NORMAL},

    {'date': '6/4/18', 'schedule': NORMAL},
]

schedule = [
    dict(entry, date=datetime.datetime.strptime(entry['date'], '%m/%d/%y').date())
    for entry in raw_schedule
]

def get_upcoming_entry():
    for entry in schedule:
        if entry['date'] >= datetime.date.today():
            return entry
