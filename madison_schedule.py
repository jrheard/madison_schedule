import datetime
from pytz import timezone


from flask import Flask
from flask_ask import Ask, statement


app = Flask(__name__)
ask = Ask(app, '/')


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



@ask.intent('GetScheduleIntent')
def get_schedule():
    schedule_entry = get_upcoming_entry()

    tz = timezone('America/Los_Angeles')
    today = tz.fromutc(datetime.datetime.utcnow()).date()

    if schedule_entry['date'] == today:
        day_string = 'today'
    elif (schedule_entry['date'] - today).days == 1:
        day_string = 'tomorrow'
    else:
        day_string = schedule_entry['date'].strftime('%A, %B %-d')

    if schedule_entry['schedule'] == NORMAL:
        schedule_string = 'normal, which means that class starts at 9:43'
    elif schedule_entry['schedule'] == FLEX:
        schedule_string = 'flex, which means that class starts at 9:30'
    else:
        schedule_string = 'weird, so you should ask tamara what time to come in'

    message = "You have class {0}. The schedule is {1}.".format(day_string, schedule_string)

    return statement(message).simple_card('Schedule', message)





if __name__ == '__main__':
    app.run()
