import json

class CmdbCiLinux():
    
    def __init__ (self, name, ip, distribution, service, action):
        self.name = name
        self.ip = ip
        self.distribution = distribution
        self.service = service
        self.action = action
        
    def get_data(self):
        return json.dumps({"Name" : self.name,
                        "IpAdress" : self.ip,
                        "Distibution" : self.distribution,
                        "Service": self.service,
                        "Action": self.action})   
