#MIT License
#
#Copyright (c) 2017 Connor Beam
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
import select
import socket
import re
import json
import pygeoip
servers = []

#For A Port Cheat Sheet Go To http://packetlife.net/media/library/23/common-ports.pdf
#Below Is The List Of Ports To Imitate Remove Or Add As You Please
portlist = [7,9,21,22,23,25,53,80,110,137,138,139,443,1434,8080]
#Above Is The List Of Ports To Imitate Remove Or Add As You Please
#IMPORTANT DO NOT CHANGE ANYTHING PAST HERE IT COULD BREAK THE PROGRAM
print("This Is Version 1.0 Of Simple HoneyPY")
print("By Connor Beam")
for port in portlist:
    ds = ("0.0.0.0", port)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ds)
    server.listen(1)

    servers.append(server)

while True:
    readable,_,_ = select.select(servers, [], [])
    ready_server = readable[0]

    connection, address = ready_server.accept()
    GEOIP = pygeoip.GeoIP("GeoIP.dat")
    IPCOUNTRY = GEOIP.country_name_by_addr(str(address[0]))
    f = open('LOG.LOG', 'a')
    f.write(str(address[0]) + "\n")
    f.close()
    print("New Connection From " + str(address[0]) + str(IPCOUNTRY) + " ALERT")
