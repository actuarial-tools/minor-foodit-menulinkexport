import binascii
import tkinter
from tkinter import messagebox
from dbfpy import dbf ,record

class DbfData(object):
    __slots__ = ("dbf", "name")

    def __init__(self, file=None):
        self.name = file
        self.dbf = dbf.Dbf(file)

    def __getitem__(self, index):
        if self.dbf is not None:
            return self.dbf[index]
        else:
            return None

    def header_length(self):
        return self.dbf.header.header_length

    def record_length(self):
        return self.dbf.header.record_length
    def record_count(self):
        return self.dbf.header.record_count

    def printInfo(self):
        if self.dbf is not None:
            print(self.dbf)
        else:
            pass

    def field_names(self):
        return self.dbf.field_names

    def pack(self):
        pass

    def remove(self,index=None,id=None,name=None):
        pass

    def add(self):
        return self.dbf.new_record()

    def update(self,record):
        self.dbf.write_record(record)

    def close(self):
        self.dbf.close()

    def seek(self,offset):
        self.dbf.stream.seek(offset)

    def read(self):
        return self.dbf.stream.read()

    def truncate(self):
        self.dbf.stream.truncate()

    def write(self,bytes):
        self.dbf.stream.write(bytes)

    def flush(self):
        self.dbf.stream.flush()

    def writable(self):
        return self.dbf.stream.writable()

    """ 
     Clear dbf Usage
     filename = "<path>\\EMP.DBF"
     dbfRec = AlohaDBF.DbfData(filename)
     dbfRec.deleteAll()
     dbfRec.writeHeaderWithCount(0)
     """
    def deleteAll(self):
        if self.dbf is not None and len(self.dbf) > 0:
            self.dbf.stream.seek(self.dbf[0].position)
            #allRec = bytearray(self.dbf.stream.read())
            #self.dbf.stream.truncate(len(allRec))
            self.dbf.stream.truncate()
        else:
            return None

    """
    Write head data file and then alert
    """
    def writeHeaderWithCount(self,recordCount):
        if isinstance(recordCount,int):
            self.dbf.stream.flush()

            if self.dbf.stream.writable():
                # write SUB (ASCII 26) after last record
                self.dbf.stream.seek(
                    self.dbf.header.header_length +
                    recordCount * self.dbf.header.record_length
                )
                self.dbf.stream.write(b"\x1A")
                self.dbf.stream.truncate()
            self.dbf.stream.close()

            #Set record count
            handleDBF = AlterHeadData()
            handleDBF.loadByteArray(str(self.name))
            handleDBF.resetRecordCount(recordCount)
            handleDBF.writeToFile()

            self.showWarning("Database file updated","The data is updated. Should close and reopen Aloha Manager for data updated")

    def showWarning(self,titleText=None,messageText=None):
        # hide main window
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showwarning("Warning"+' '+titleText, str(messageText))



"""
    Used for POS dbf as foxpro dbase
    Steps are load,resetcount ,writebacktofile 
"""
class AlterHeadData(object):

    def __init__(self):
        #byte array
        self.mutable_bytes = None
        self.record_count_hex = None
        self.relativefilename = None

    def loadByteArray(self,relativefilename):
        try:
            self.relativefilename = relativefilename
            with open(self.relativefilename, "rb") as binary_file:
                #For seek to position ,binary_file.seek(4)
                self.mutable_bytes = bytearray(binary_file.read())
            #print("Load file %s." % self.relativefilename)
        except:
           self.mutable_bytes = None

    """
       Convert record count no (integer) to format hex string
       Exp : 
       input as 2073
       output as 19080000
    """
    def resetRecordCount(self,recordCount):
        #Other way : print(struct.pack(">I", 4003).encode('hex'))
        hex4bytes = '{:08x}'.format(recordCount)
        self.record_count_hex = hex4bytes[6:]+hex4bytes[4:6]+hex4bytes[2:4]+hex4bytes[0:2]
        #print("Recal record count to %s." %self.record_count_hex)
        if self.mutable_bytes is not None:
            self.mutable_bytes[4] = int(hex4bytes[6:],16)
            self.mutable_bytes[5] = int(hex4bytes[4:6],16)
            self.mutable_bytes[6] = int(hex4bytes[2:4],16)
            self.mutable_bytes[7] = int(hex4bytes[0:2],16)
            #print(str(self.mutable_bytes[4])+" "+str(self.mutable_bytes[5])+" "+str(self.mutable_bytes[6])+" "+str(self.mutable_bytes[7]))


    def writeToFile(self):
        if self.mutable_bytes is not None:
            #b'/x0F/xFF'
            immutable_bytes = bytes(self.mutable_bytes)
            #print(str(immutable_bytes))
            with open(self.relativefilename, "wb") as binary_file:
                num_bytes_written = binary_file.write(immutable_bytes)
                #print("Wrote %d bytes." % num_bytes_written)


""" [Delete case]
with open(argv[0], "rb") as binary_file:
    print('file size '+ str(len(bytearray(binary_file.read()))) )

db = dbf.Dbf(argv[0])

tempRec100 = db[100]
#tempRec100.delete()
#db.write_record(tempRec100)

del_start = tempRec100.position
del_len = len(tempRec100.to_bytes())
next_offset = del_start+del_len
print('offset start ' +str(del_start))
print('record size ' + str(del_len))
print('next offset ' + str(next_offset))

db.stream.seek(next_offset)
#print(db.stream.tell())
dataTrail = db.stream.read()
print('trail size ' + str(len(dataTrail)))

db.stream.seek(del_start + 0)
#print(db.stream.tell())
db.stream.truncate()
print('current offset '+str(db.stream.tell()) )
print('can read ' + str(len(bytearray(db.stream.read()))))

db.stream.write(dataTrail)
print('current offset ' + str(db.stream.tell()))

newRecordCount = db.record_count - 1

db.stream.flush()

if db.stream.writable():
    # write SUB (ASCII 26) after last record
    db.stream.seek(
        db.header.header_length +
        newRecordCount * db.header.record_length
    )
    db.stream.write(b"\x1A")
    db.stream.truncate()
db.stream.close()

handleDBF = AlohaDBF.AlterHeadData()
handleDBF.loadByteArray(str(argv[0]))
handleDBF.resetRecordCount(newRecordCount)
handleDBF.writeToFile()

db = dbf.Dbf(argv[0])
print(db.record_count)
#print(db)

#pack()

"""

""" [Create case]
  db = dbf.Dbf(argv[0])
  print(db.record_count)
  orgRec100 = db[100]
  tempRec100 = db[100]
  tempRec100.delete()
  db.write_record(tempRec100)

  tempRec101 = db[101]
  tempRec101.delete()
  db.write_record(tempRec101)

  max = 0.0
  lastrecord = None
  for record in db:
      max ,lastrecord = getMax(record,max,lastrecord)

  rec = db.new_record()
  for fieldName in db.field_names:
      rec[fieldName] = lastrecord[fieldName]
  rec[b'ID'] = max+1
  rec[b'USERNUMBER'] = max+1 
  rec[b'SHORTNAME'] = 'Special panda salad'
  rec[b'CHITNAME'] = 'Special panda salad'
  rec[b'LONGNAME'] = 'Special panda salad'
  db.write_record(rec)

  rec2 = db.new_record()
  for fieldName in db.field_names:
      rec2[fieldName] = orgRec100[fieldName]
  db.write_record(rec2)

  #db.write_record(orgRec100)
  print(db.record_count)

  newRecordCount = db.record_count
  db.close()

  handleDBF = AlohaDBF.DbfData()
  handleDBF.loadByteArray(str(argv[0]))
  print('recal record count %s in header '% newRecordCount)
  handleDBF.resetRecordCount(newRecordCount)
  handleDBF.writeToFile()
  """
