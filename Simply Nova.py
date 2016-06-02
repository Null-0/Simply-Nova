from novaclient.client import Client
import time

## Good luck using this to hack me;  Syntax for this client is: version, username, pw, project, url
nova_client = Client("2","admin","977e4e695fdc4936","admin","http://10.5.7.18:5000/v2.0")
def find_servers():
    find_time= time.strftime("%m%d%y-%H")
    open_log_file=open(find_time,"w")
    n=0
    try:
        collect_server_list = (nova_client.servers.list())
        for table in collect_server_list:
           print(table,":",nova_client.servers.ips(table),end="\n",file=open_log_file)
        open_log_file.close()
    except:
        print("Failure has occurred, pausing for 8 hours until admin can look into this",end="",file=open_log_file)
        time.sleep(28800)
        find_servers()
find_servers()
