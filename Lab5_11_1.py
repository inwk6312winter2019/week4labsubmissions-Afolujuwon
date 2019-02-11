class IPv4address():
        def __init__(self,ip=[0,0,0,0],nm=[0,0,0,0]):
                self.ip=ip
                self.nm=nm
        def __str__(self):
                ipformat=""
                for ips in self.ip:
                        ipformat=ipformat+str(ips)+"."
                return('the address is:'+ ipformat)
        def getNetwork(self,nadd=[0,0,0,0]):
                self.nadd=nadd[0:3]
                return self.nadd
        def getMask(self,mask=[0,0,0,0]):
                self.mask=self.nm
                return self.mask
        def getAddress(self,ipadd=[0,0,0,0]):
                self.ipadd=self.ip
                return self.ipadd

myip=IPv4address([192,168,1,1],[255,255,255,255])
mynw=myip.getNetwork([192,168,10,5])
mymask=myip.getMask()
myipad=myip.getAddress()
print(myip)
print(mynw)
print(mymask)
print(myipad)
