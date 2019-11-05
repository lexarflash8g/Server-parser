
def readfile(file):

  servers = []

  servers_1 = []
  with open(file, 'rt') as filename:
    for line in filename:
      text1 = line.replace('=', '.')
      line3 = text1.split('.')
      #z = line3.strip('*')
      y = ([x for x in line3 if x!= '*'])
      z = [x.strip(' ') for x in y]
      z[-1] = z[-1].strip()
      servers.append(z)

   # for server in servers:
    #    server_l = server.strip('*')
     #   servers_1.append(server_1)

    return servers
filename= input(" which file in txt format  for input?")

servers = readfile(filename)

#get serveres and then sort by number of elements such
#as [customer1.us.ca.sjc], ['customer2.us.ca.*'].. we can search list from most elements to least
servers.sort(key = len)
servers.reverse()


def input_format(input_1):

  text1= (input_1.replace('=', '.'))
  input_2 = text1.split('.')
  return (input_2)

input_1 = input("what server to check for input?")
input = input_format(input_1)


def loadConfig():

    for server in servers:

      if input[-1] in server and len(server) == 5:
        return server[-1]
        break

      else:
        if (input[-2] in server) and (len(server) == 4):
          return server[-1]
     # print(server)
          break
        else:
           if (input[-3] in server) and (len(server) == 3):
             return server[-1]
             break
           else:
             if (input[-4] in server) and (len(server) == 2):
               return server[-1]
               break
             elif len(server)==1:
               return server[-1]

server = loadConfig()
print(server)
