from flask import  *
import sys
sys.path.insert(0, 'lib')
from pyfcm import FCMNotification




app = Flask(__name__)
@app.route('/send',methods = ['POST'])
def send_message():
    msg = request.form['msg']
    push_service = FCMNotification(api_key="<check email>")
    result = push_service.notify_topic_subscribers(topic_name="all", message_body=msg,message_title="HuHuba Problem - siddharths067")
    #print result
    return msg
        

@app.route('/')
def hello_world():
    return render_template('send.html')

if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1',8081)
