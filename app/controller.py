from app import app
from Flask import render_template
from app.models.event_list import events, add_event
from app.models.event import *

@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events)

