from app import app
from Flask import render_template
from app.models.event_list import events, add_event

@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events)

