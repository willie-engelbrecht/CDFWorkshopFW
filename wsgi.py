#!/usr/bin/python3

from flask import Flask
from flask import request
import requests
import subprocess

app = Flask(__name__)

@app.route("/eventcode", methods = ['POST'])
def eventcode():
    if request.method == 'POST':
        eventcode = request.form['eventcode']
           
        f = open("/etc/wkey", "r")
        wkey = f.read()
        f.close()

        if eventcode.strip().lower() == wkey.strip().lower():
            r = requests.get('http://ipinfo.io/hostname')

            remote_ip = request.remote_addr

            f = open("/etc/sg1", "r")
            sg1 = f.read()
            f.close()
            subprocess.call("/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id "+ sg1.strip() +" --protocol tcp --port 1-65535 --cidr " + remote_ip+"/32", shell=True)
            
            f = open("/etc/sg2", "r")
            sg2 = f.read()
            f.close()
            subprocess.call("/usr/local/bin/aws ec2 authorize-security-group-ingress --group-id "+ sg2.strip() +" --protocol tcp --port 1-65535 --cidr " + remote_ip+"/32", shell=True)

            return '<meta http-equiv="refresh" content="0; URL=\'http://' + r.text +'\'" />'
        else:
            return entry()


@app.route("/")
def entry():
    return '''
<!DOCTYPE html>
<html>
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  font-size: large;
}

input[type=submit] {
  width: 100%;
  background-color: #f96702;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: large;
}

input[type=submit]:hover {
  background-color: #c55203;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;

  display: block;
  margin-left: auto;
  margin-right: auto;
  margin-top: 100px;
  width: 50%;
  padding: 20px 10px;
}
</style>
<body>

<div>
  <form action="/eventcode" method="post">
    <input type="text" id="eventcode" name="eventcode" placeholder="Event Registration Code...">

  
    <input type="submit" value="Submit">
  </form>
</div>

</body>
</html>
'''


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8443', debug=True)
    app.run()
