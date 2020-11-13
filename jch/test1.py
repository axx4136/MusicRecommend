def getOpcode(self):
    first8Bit = self.con.recv(1)
    first8Bit = struct.unpack('B', first8Bit)[0]
    opcode = first8Bit & 0b00001111
    return opcode
def getDataLength(self):
    second8Bit = self.con.recv(1)
    second8Bit = struct.unpack('B', second8Bit)[0]
    masking = second8Bit >> 7
    dataLength = second8Bit & 0b01111111
    #print("dataLength:",dataLength)
    if dataLength <= 125:
        payDataLength = dataLength
    elif dataLength == 126:
        payDataLength = struct.unpack('H', self.con.recv(2))[0]
    elif dataLength == 127:
        payDataLength = struct.unpack('Q', self.con.recv(8))[0]
    self.masking = masking
    self.payDataLength = payDataLength    
def readClientData(self):

    if self.masking == 1:
        maskingKey = self.con.recv(4)
    data=self.con.recv(self.payDataLength)

    if self.masking == 1:
        i = 0
        trueData = ''
        for d in data:
            trueData += chr(d ^ maskingKey[i % 4])
            i += 1
        return trueData
    else:
        return data
def sendDataToClient(self, text):
    sendData = ''
    sendData = struct.pack('!B', 0x81)

    length = len(text)
    if length <= 125:
        sendData += struct.pack('!B', length)
    elif length <= 65536:
        sendData += struct.pack('!B', 126)
        sendData += struct.pack('!H', length)
    elif length == 127:
        sendData += struct.pack('!B', 127)
        sendData += struct.pack('!Q', length)

    sendData += struct.pack('!%ds' % (length), text.encode())
    dataSize = self.con.send(sendData)
