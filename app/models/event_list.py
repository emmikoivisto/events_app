from app.models.event import Event

event_1 = Event("2020-03-16", "Slumber party", 6, "Campus", "Party time!")
event_2 = Event("2020-01-28", "Concert", 128, "O2 Arena", "My favourite pop band")
events = [event_1, event_2]

def add_event(event):
    events.append(event)