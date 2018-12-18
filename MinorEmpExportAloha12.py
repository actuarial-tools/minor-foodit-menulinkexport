import sys
import os
import decimal
import numbers

import logging
import logging.handlers as handlers
import time
from tkinter import Label,Button, Tk, HORIZONTAL ,messagebox
from tkinter.ttk import Progressbar
import threading

#from dbfread import DBF
from minor import Configure
from minor import MSQL
from minor import AlohaDBF
from minor.model import DBF
from minor.dbfstore import dbf ,record

import json
import pyodbc
import configparser

#Other sub class

# append module root directory to sys.path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
"""
    [b'ID', b'OWNERID', b'USERNUMBER', b'SEC_NUM', b'SSN', b'SSNTEXT', b'FIRSTNAME', b'MIDDLENAME', b'LASTNAME', b'NICKNAME', b'ADDRESS1', b'ADDRESS2', b'CITY', b'STATE', b'ZIPCODE', b'PHONE', b'COUNTRY', b'COUNTRYCDE', b'LOCALEID', b'BIRTHDAY', b'DATEOFHIRE', b'LASTACCES
    S', b'PASSWORD', b'MAGCARD', b'SECURITY', b'TIPS', b'QWERTY', b'WKTOTMIN', b'WKTOVMIN', b'WKDOVMIN', b'WKTOTPAY', b'WKTOVPAY', b'WKDOVPAY', b'JOBCODE1', b'JOBCODE2', b'JOBCODE3', b'JOBCODE4', b'JOBCODE5', b'JOBCODE6', b'JOBCODE7', b'JOBCODE8', b'JOBCODE9', b'JOBCODE10
    ', b'PAYRATE1', b'PAYRATE2', b'PAYRATE3', b'PAYRATE4', b'PAYRATE5', b'PAYRATE6', b'PAYRATE7', b'PAYRATE8', b'PAYRATE9', b'PAYRATE10', b'ACCESS1', b'ACCESS2', b'ACCESS3', b'ACCESS4', b'ACCESS5', b'ACCESS6', b'ACCESS7', b'ACCESS8', b'ACCESS9', b'ACCESS10', b'SKILL1', b'
    SKILL2', b'SKILL3', b'SKILL4', b'SKILL5', b'SKILL6', b'SKILL7', b'SKILL8', b'SKILL9', b'SKILL10', b'PREF1', b'PREF2', b'PREF3', b'PREF4', b'PREF5', b'PREF6', b'PREF7', b'PREF8', b'PREF9', b'PREF10', b'MEALS', b'MEALPCNT', b'TERMINATED', b'ZAPID', b'REHIRE', b'LASTDAY'
    , b'RTNDAY', b'ZAPEXPLN', b'XFERUNIT', b'MOVE', b'MARITAL', b'NUMDEPEND', b'EXEMPT', b'WITHEXTRA', b'VETRANSTAT', b'MAGONLY', b'DDLRFEE', b'DPRCNTFEE', b'DMLGFEE', b'DDLEXP', b'DINSRNCEXP', b'SEX', b'JOBSTATUS', b'EMPCODE1', b'EMPCODE2', b'BOHPASSWRD', b'SECLEVEL', b'
    STARTTIME', b'ENDTIME', b'PWDCHANGE', b'PENID', b'TEAMSORT', b'TEAMLMTREV', b'ADDRESS3', b'ADDRESS4', b'COUNTY', b'THUMBSCCI', b'WORKPOLID', b'EMPTYPEID', b'THUMBSCLI', b'REMARKS', b'SCHEDSTART', b'SCHEDEND', b'EMPCODE3', b'EMPCODE4', b'EMPCODE5', b'WAIVEMBRK', b'LAST
    CHPSWD', b'BOHLASTPWD', b'NCFLOGON', b'SSN_ENC', b'EMPLIQCERT', b'EMPLIQEXP', b'MINORXMT', b'BOHHASHPW', b'EXP_ID']
"""
JOBCODE = ['JOBCODE1', 'JOBCODE2', 'JOBCODE3', 'JOBCODE4', 'JOBCODE5', 'JOBCODE6', 'JOBCODE7', 'JOBCODE8','JOBCODE9', 'JOBCODE10']
PAYRATE = ['PAYRATE1', 'PAYRATE2', 'PAYRATE3', 'PAYRATE4', 'PAYRATE5', 'PAYRATE6', 'PAYRATE7', 'PAYRATE8','PAYRATE9', 'PAYRATE10']
ACCESS  = ['ACCESS1', 'ACCESS2', 'ACCESS3', 'ACCESS4', 'ACCESS5', 'ACCESS6', 'ACCESS7', 'ACCESS8', 'ACCESS9','ACCESS10']
DBF_FILE = {"EMP":"EMP.DBF"}
CREATED_ROWS = []


""" [DBread]
    table = DBF('D:\projects\Aloha\DATA\ITM.DBF',encoding='cp1252',load=True)
    print(table.records[0])
    for record in DBF('D:\projects\Aloha\DATA\ITM.DBF',encoding='cp1252'):
        print(record)
    db = dbf.Dbf("E:\\Aloha\\Deployed\\SZ\\20181127\\nextToLab\\ITM.DBF")

def getMax(record,max,tmprecord):
    if(record[b'ID']>max):
       #print(type(record[b'ID']) , type(max)) 
       #print(record[b'ID']>max)
       if( record[b'ID']   < 20000.0):
         max = record[b'ID']  
         tmprecord =  record
    return max ,tmprecord

def printall(db):
    print(db, '\n')
    #print(db.record_count)
    #print(db.field_names)
"""

"""
[Convert key as bytes to str] 

def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    elif isinstance(data, dict):
        return dict(map(convert, data.items()))
    elif isinstance(data, tuple):
        return map(convert, data)
    else:
        return data
"""

"""JSON
def writeJson(db,outfilename):
    item_list = []
    for record in db:
        item_list.append(convert(record.as_dict()))

    with open(outfilename, 'w') as outfile:
        json.dump(item_list, outfile, indent=4)

def loadJson(readfilename):
    data = None
    with open(readfilename) as json_file:
        data = json.load(json_file)
    return data
"""

"""Loop to action
def for_loop_action_todo(iterable, action_to_do,db):
    iterator = iter(iterable)
    done_looping = False
    while not done_looping:
        try:
            item = next(iterator)
        except StopIteration:
            done_looping = True
        else:
            action_to_do(item,db)

def overwriteRecord(item,db):
    #Find filter by ID
    found = filter(lambda record: record[b'ID'] == item.get("ID"), db)
    isExist = any(True for _ in found)
    if isExist:
        print('update' + str(item.get("ID")))
        for recordFilter in found:
            doUpdateWith(recordFilter,item)
    else:
        print('create' + str(item.get("ID")))
        doCreate()
"""

"""JSON 
# x = Items.ItemObject()
# writeJson(db,'items.json')
# jsonData = loadJson('items.json')
# for_loop_action_todo(jsonData,overwriteRecord,db)
"""

def pack():
   pass

def getSQLConn(config):
    SQLConn = MSQL.SqlDb(config.ConfigSectionMap("MenuLink")['host']
                         , config.ConfigSectionMap("MenuLink")['database']
                         , config.ConfigSectionMap("MenuLink")['user']
                         , config.ConfigSectionMap("MenuLink")['password'])
    return SQLConn

def loopOnDBF(listOf_EmpID_Query,openfile):
    db = AlohaDBF.DbfData(openfile)
    found = list(filter(lambda record: record[b'MIDDLENAME'][0:3] == "SSN" or record[b'MIDDLENAME'][0:4] == "กรอก", db))
    #log("Loop employee size=" + str(len(found)))
    db.close()
    for rec in found:
        #log("Finding rec_ID " + str(rec[b'ID']))
        matchID = list(filter(lambda ID: float(ID) == rec[b'ID'], listOf_EmpID_Query))
        #log(len(matchID))
        isExist = any(True for _ in matchID)
        #log(isExist)
        if not isExist:
            log("Record deleted ,ID=" + str(int(rec[b'ID'])))
            doRemove(rec[b'ID'], openfile)


def loopOnRecord(model,db):
    global hasNewRecordCreated
    #Find filter by ID
    found = list(filter(lambda record: record[b'ID'] == float(model.ID), db))
    isExist = any(True for _ in found)
    if isExist:
        log("Record updated ,ID="+str(model.ID))
        #model is DBF.enp
        for recordFilter in found:
            doUpdateWith(recordFilter,model)
    else:
        log("Record created ,ID=" + str(model.ID))
        hasNewRecordCreated = True
        CREATED_ROWS.append(model.ID)
        doCreate(model,db)

def doRemove(id_val,openfile):
    db = AlohaDBF.DbfData(openfile)
    rec = list(filter(lambda record: id_val == record[b'ID'],db))[0]
    offset_start = rec.position
    bytesDeleted = len(rec.to_bytes())
    offset_next_rec = offset_start + bytesDeleted
    #log("Offset["+str(offset_start)+"] ,delete "+str(bytesDeleted)+" bytes ,next offset["+str(offset_next_rec)+"]" )

    #Keep remaining
    db.seek(offset_next_rec)
    bytesRemaining = db.read()

    #Delete
    db.seek(offset_start + 0)
    db.truncate()
    db.write(bytesRemaining)
    #log("Write remaining "+str(len(bytearray(bytesRemaining))))

    newRecordCount = db.record_count() - 1
    #log("Update record size is "+str(newRecordCount))
    db.flush()

    if db.writable():
        # write SUB (ASCII 26) after last record
        db.seek(
            db.header_length() +
            newRecordCount * db.record_length()
        )
        db.write(b"\x1A")
        db.truncate()


    handleDBF = AlohaDBF.AlterHeadData()
    handleDBF.loadByteArray(openfile)
    handleDBF.resetRecordCount(newRecordCount)
    handleDBF.writeToFile()

def doCreate(model,db):
    try:
        doUpdateJOBCode(model)
        doUpdateStatus(model)
        model_rec = model.dict_rec  # { keyname:value }
        rec = db.add()
        for k, v in byteKey_Map_StrKey.items():
            if isinstance(rec[k], float):
                rec[k] = float(model_rec.get(v))
            else:
                rec[k] = model_rec.get(v)
            # log(type(rec[k]))
        db.update(rec)
    except (RuntimeError, TypeError, NameError):
        log("Error:doCreate function")
        pass

def doUpdateWith(recordFilter,model):
    try:
        doUpdateJOBCode(model)
        doUpdateStatus(model)
        dict_rec = recordFilter.as_dict()
        #model_key = model.dict_key
        model_rec = model.dict_rec
        for k,v in dict_rec.items(): # b'ID' = 9900
            if( isinstance(recordFilter[k],float)):
                if model_rec.get(byteKey_Map_StrKey.get(k)) is not None:
                    recordFilter[k] = float(model_rec.get(byteKey_Map_StrKey.get(k)))
                else:
                    print(model_rec.get(byteKey_Map_StrKey.get(k)))
            else:
                if k != b'PASSWORD' and k != b'MAGCARD' and k != b'BOHPASSWRD':
                    recordFilter[k] = model_rec.get(byteKey_Map_StrKey.get(k))
            dbfRec.update(recordFilter)
    except (RuntimeError, TypeError, NameError):
        log("Error:doUpdate function")
        pass

def doUpdateJOBCode(model):
    connProp = SQLConn.createConn()
    cursorProp = SQLConn.getEmpProperty(model.HOMESITE_NUMBER,model.EMPLOYEE_NUMBER,connProp)
    for idx,row in enumerate(cursorProp):
        if idx <= 9:
            model.dict_rec[JOBCODE[idx]] = row[3]
            model.dict_rec[PAYRATE[idx]] = row[4]
            model.dict_rec[ACCESS[idx]]  = row[9]
        else:
            break

def doUpdateStatus(model):
    connStatus = SQLConn.createConn()
    cursorStatus = SQLConn.getStatus(model.HOMESITE_NUMBER, model.EMPLOYEE_NUMBER, connStatus)
    for row in cursorStatus:
        model.dict_rec['JOBSTATUS'] = row[0]

def doWriteCreated(db):
    global filename
    #print("Created row size update is "+str(db.record_count()))
    newRecordCount = db.record_count()
    db.close()

    #log("Write updated file name "+ str(filename))
    handleDBF = AlohaDBF.AlterHeadData()
    handleDBF.loadByteArray(filename)
    handleDBF.resetRecordCount(newRecordCount)
    handleDBF.writeToFile()

def log(message):
    Configure.logger.info(str(message))


class MonApp(Tk):
    def __init__(self,argv):
        super().__init__()
        self.iconbitmap(default='minor\logo_minor.ico')
        self.winfo_toplevel().title("Minor FoodIT - MenuLink Export Data (2018 Copy@Right)")
        self.geometry("500x30") #You want the size of the app to be 500x500
        self.resizable(0, 0)  # Don't allow resizing in the x or y direction
        self.btn = Button(self, text='Exporting data', command=self.start)
        self.btn.grid(row=0,column=0)
        self.label = Label(self,text="")
        self.label.grid(row=0, column=2)
        self.progress = Progressbar(self, orient=HORIZONTAL,length=200,  mode='indeterminate')
        self.argv = argv


    def start(self):
        def real_start():
            self.progress.grid(row=0,column=1)
            self.progress.start()
            self.label['text'] = 'Data processing...'
            #time.sleep(5)
            main_run(self.argv)
            #Move to main_run
            self.quit()

        self.btn['state']='disabled'
        threading.Thread(target=real_start).start()

        def main_run(argv):
            # log("Original file record size is "+str(dbfRec.record_count()))
            if menulink_ver <= 15 and aloha_ver >= 12:
                conn = SQLConn.createConn()
                # Check exist from query to file

                cursor = SQLConn.getEmpData(conn, site_number)
                for row in cursor:
                    empQuery = DBF.Emp(row)
                    loopOnRecord(empQuery, dbfRec)
                #log("hasNewRecordCreated is " + str(hasNewRecordCreated))
                if hasNewRecordCreated:
                    doWriteCreated(dbfRec)
                else:
                    dbfRec.close()
                # log("File updated/created record size is " + str(dbfRec.record_count()))

                # Check file to removed
                openfile = filename
                cursor = SQLConn.getEmpData(conn, site_number)
                cursorID = [row[0] for row in cursor]
                loopOnDBF(cursorID, openfile)
                db = AlohaDBF.DbfData(openfile)
                # log("File deleted record size is " + str(db.record_count()))

                self.progress.stop()
                self.progress.grid_forget()
                self.label['text'] = 'Done.'
                self.btn['state'] = 'normal'

                dbfRec.showWarning("Database file updated",
                                   "The data " + str(DBF_FILE.get(
                                       sys.argv[1:][0])) + " is updated. Please refresh data in Aloha Configuration Center to load updated")
            elif menulink_ver >= 15 and aloha_ver < 12:
                log("to be future")
            else:
                pass

if __name__ == "__main__":
    hasNewRecordCreated = False
    try:
        log("############# Start Running")
        log("Load configuration file config.ini")
        config = Configure.ConfigureData("config.ini")

        site_number = config.ConfigSectionMap("Minor")['site_number']
        menulink_ver = float(config.ConfigSectionMap("MenuLink")['version'])
        aloha_ver = float(config.ConfigSectionMap("Aloha")['version'])
        log("MunuLink version " + str(menulink_ver))
        log("Aloha version " + str(aloha_ver))

        newdata_location = config.ConfigSectionMap("Aloha")['newdata_path']
        filename = newdata_location + "\\" + str(DBF_FILE.get(sys.argv[1:][0]))
        log("Exporting data to " + filename)
        dbfRec = AlohaDBF.DbfData(filename)
        """
        for i in dbfRec.field_names():
            name = str(i)
            log(name+":"+str(dbfRec[10][i]))
        #log(dbfRec.printInfo())
        """

        # List field
        byte_field_name = dbfRec.field_names()
        byteKey_Map_StrKey = {bkey: bkey.decode(encoding='utf-8', errors='strict') for idx, bkey in
                              enumerate(byte_field_name)}

        SQLConn = getSQLConn(config)

    except IndexError:
        log("Error:DBF file is required ,please assign with options")
        raise SystemExit("DBF file is required ,please assign with options.\n Example: toolExport.exe EMP")
    except FileNotFoundError:
        log("The DBF File is not found")
        raise SystemExit("The DBF File is not found")

    app = MonApp(sys.argv[1:])
    app.mainloop()

    #main(sys.argv[1:])
    log("Finished")




