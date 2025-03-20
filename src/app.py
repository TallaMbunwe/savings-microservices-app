# Importing socket library
import socket

from flask import Flask,jsonify, render_template

app = Flask(__name__)


# Function to display hostname and IP address
 
 
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        #print("Hostname :  ", host_name)
        #print("IP : ", host_ip)
    except:
        print("Unable to get Hostname and IP")

    return host_name, host_ip
 
 
# Driver code
#get_Host_name_IP()  # Function call


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify (
        status="UP"
    )

@app.route("/details")
def details():
    hostName, hostIp = get_Host_name_IP()
    return render_template('index.html', HOSTNAME=hostName, HOSTIP=hostIp)
 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)