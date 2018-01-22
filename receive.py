import serial,string,time
output = ""
ser = serial.Serial('/dev/serial0',9600,8,'N',1,timeout=1)

while True:
    
    print 'waiting'
    
    #query = raw_input('Enter your input:')
    
    #ser.write(query + '\n')

    time.sleep(1)
    print "Buffer ="+str(ser.inWaiting())

    if ser.inWaiting() >0:
        output = ser.read(10)
        print output
        time.sleep(3)
        
    #Trial 1st


