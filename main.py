import jinja2
import flask
import waitress
import db_utils

PAGE_PATH = 'index.html' 
SCRIPT_PATH = 'script.js' 
CSS_PATH = 'style.css' 
JQUERY_URL = 'https://code.jquery.com/jquery-3.4.1.min.js' 
OWN_PATH = '0.0.0.0'

app = flask.Flask(__name__) 

rdb = db_utils.ReportDatabase('reports.db') 

@app.route('/remove_id/<ID>') 
def remove_by_id(ID): 
    rdb.delete(ID) 

@app.route('/')
def home(): 
    with open(PAGE_PATH) as page_file, open(SCRIPT_PATH) as script_file, \
open(CSS_PATH) as style_file: 
        templ = jinja2.Template(page_file.read()) 
        script_text = script_file.read() 
        style_text = style_file.read() 

    items = rdb.items() 

    return templ.render(data=items, dbstyle_text=style_text, script_text=script_text, jq_source=JQUERY_URL)   

app.run(port=8000) 