from flask import Flask
import datetime
 
date = datetime.datetime.now()
 
app = Flask(__name__)
 
 
@app.route('/data')
def get_time():
 
    return {
        'Name':"geek",
        "Age":"22",
        "Date":date,
        "programming":"python"
        }
 
 
if __name__ == '__main__':
    app.run(debug=True)