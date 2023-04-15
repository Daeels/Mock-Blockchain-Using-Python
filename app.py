from flask import *
from blockchain import *
from CmdbCiLinux import *
import json

#__Config
app = Flask(__name__)

# Create the blockchain
b = BlockChain()


@app.route("/block", methods=["POST"])
def block():
    name = request.form.get("name")
    ip = request.form.get("ip adress")
    dis = request.form.get("distribution")
    ser = request.form.get("service")
    action = request.form.get("action")
    cmdbcilinux01 = CmdbCiLinux(name=name, ip=ip, distribution=dis, service=ser,action=action)
    b.addNewBlock(cmdbcilinux01.get_data())
        
    return "Block created!"


@app.route("/mine", methods=["POST"])
def mine():
    
    b.mineChain()
    chain = b.printBlockChain()
    return json.dumps(chain)


@app.route("/chain", methods=["POST"])
def chain():
    
    chain = b.printBlockChain()
    return json.dumps(chain)


@app.route("/verify", methods=["POST"])
def verify():
    
    count = b.verify_chain()
    if count != 0 :
        return "Clean"
    else :
        return "Broken\nThe chain is broken!"
    
    
@app.route("/change_data", methods=["POST"])
def change():
    no = int(request.form.get("no"))
    name = request.form.get("name")
    ip = request.form.get("ip adress")
    dis = request.form.get("distribution")
    ser = request.form.get("service")
    action = request.form.get("action")
    
    cmdbcilinux01 = CmdbCiLinux(name=name, ip=ip, distribution=dis, service=ser,action=action)
    
    b.changeData(no, cmdbcilinux01.get_data())
    
    return "Data is modified!"


if __name__ == "__main__":
    app.run(debug=True)
