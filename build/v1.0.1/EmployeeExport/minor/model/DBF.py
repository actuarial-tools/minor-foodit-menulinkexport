import minor.Configure

class Emp:
    __slots__ = ("ID","OWNERID","USERNUMBER","SEC_NUM","SSN","SSNTEXT","FIRSTNAME","MIDDLENAME","LASTNAME","NICKNAME"
                 ,"ADDRESS1","ADDRESS2","CITY","STATE","ZIPCODE","PHONE","COUNTRY","COUNTRYCDE","LOCALEID","BIRTHDAY"
                 ,"DATEOFHIRE","LASTACCESS","PASSWORD","MAGCARD"
                 ,"SECURITY","TIPS","QWERTY","WKTOTMIN","WKTOVMIN","WKDOVMIN","WKTOTPAY","WKTOVPAY","WKDOVPAY"
                 ,"JOBCODE1","JOBCODE2","JOBCODE3","JOBCODE4","JOBCODE5","JOBCODE6","JOBCODE7","JOBCODE8","JOBCODE9","JOBCODE10"
                 ,"PAYRATE1","PAYRATE2","PAYRATE3","PAYRATE4","PAYRATE5","PAYRATE6","PAYRATE7","PAYRATE8","PAYRATE9","PAYRATE10"
                 ,"ACCESS1","ACCESS2","ACCESS3","ACCESS4","ACCESS5","ACCESS6","ACCESS7","ACCESS8","ACCESS9","ACCESS10"
                 ,"SKILL1","SKILL2","SKILL3","SKILL4","SKILL5","SKILL6","SKILL7","SKILL8","SKILL9","SKILL10"
                 ,"PREF1","PREF2","PREF3","PREF4","PREF5","PREF6","PREF7","PREF8","PREF9","PREF10"
                 ,"MEALS","MEALPCNT","TERMINATED","ZAPID","REHIRE"
                 ,"LASTDAY","RTNDAY","ZAPEXPLN"
                 ,"XFERUNIT","MOVE","MARITAL","NUMDEPEND","EXEMPT","WITHEXTRA","VETRANSTAT","MAGONLY"
                 ,"DDLRFEE","DPRCNTFEE","DMLGFEE","DDLEXP","DINSRNCEXP"
                 ,"SEX","JOBSTATUS","EMPCODE1","EMPCODE2","BOHPASSWRD","SECLEVEL"
                 ,"STARTTIME","ENDTIME","PWDCHANGE","PENID","TEAMSORT","TEAMLMTREV"
                 ,"ADDRESS3","ADDRESS4","COUNTY"
                 ,"THUMBSCCI","WORKPOLID","EMPTYPEID","THUMBSCLI"
                 ,"REMARKS","SCHEDSTART","SCHEDEND","EMPCODE3","EMPCODE4","EMPCODE5"
                 ,"WAIVEMBRK","LASTCHPSWD","BOHLASTPWD","NCFLOGON"
                 ,"SSN_ENC","EMPLIQCERT","EMPLIQEXP","MINORXMT","BOHHASHPW","EXP_ID","EMPLOYEE_NUMBER","HOMESITE_NUMBER","dict_key","dict_rec")


    """
    Pass pyodb cursor
    """
    def __init__(self,row):
        if len(row) <= 141:
            #minor.Configure.logger.info("Query result = "+str(row))
            self.dict_key = {0: 'ID', 1: 'OWNERID', 2: 'USERNUMBER', 3: 'SEC_NUM', 4: 'SSN', 5: 'SSNTEXT', 6: 'FIRSTNAME', 7: 'MIDDLENAME', 8: 'LASTNAME', 9: 'NICKNAME', 10: 'ADDRESS1', 11: 'ADDRESS2', 12: 'CITY', 13: 'STATE', 14: 'ZIPCODE', 15: 'PHONE', 16: 'COUNTRY', 17: 'COUNTRYCDE', 18: 'LOCALEID', 19: 'BIRTHDAY', 20: 'DATEOFHIRE', 21: 'LASTACCESS', 22: 'PASSWORD', 23: 'MAGCARD', 24: 'SECURITY', 25: 'TIPS', 26: 'QWERTY', 27: 'WKTOTMIN', 28: 'WKTOVMIN', 29: 'WKDOVMIN', 30: 'WKTOTPAY', 31: 'WKTOVPAY', 32: 'WKDOVPAY', 33: 'JOBCODE1', 34: 'JOBCODE2', 35: 'JOBCODE3', 36: 'JOBCODE4', 37: 'JOBCODE5', 38: 'JOBCODE6', 39: 'JOBCODE7', 40: 'JOBCODE8', 41: 'JOBCODE9', 42: 'JOBCODE10', 43: 'PAYRATE1', 44: 'PAYRATE2', 45: 'PAYRATE3', 46: 'PAYRATE4', 47: 'PAYRATE5', 48: 'PAYRATE6', 49: 'PAYRATE7', 50: 'PAYRATE8', 51: 'PAYRATE9', 52: 'PAYRATE10', 53: 'ACCESS1', 54: 'ACCESS2', 55: 'ACCESS3', 56: 'ACCESS4', 57: 'ACCESS5', 58: 'ACCESS6', 59: 'ACCESS7', 60: 'ACCESS8', 61: 'ACCESS9', 62: 'ACCESS10', 63: 'SKILL1', 64: 'SKILL2', 65: 'SKILL3', 66: 'SKILL4', 67: 'SKILL5', 68: 'SKILL6', 69: 'SKILL7', 70:'SKILL8', 71: 'SKILL9', 72: 'SKILL10', 73: 'PREF1', 74: 'PREF2', 75: 'PREF3', 76: 'PREF4', 77: 'PREF5', 78: 'PREF6', 79: 'PREF7', 80: 'PREF8', 81: 'PREF9', 82: 'PREF10', 83: 'MEALS', 84: 'MEALPCNT', 85: 'TERMINATED', 86: 'ZAPID', 87: 'REHIRE', 88: 'LASTDAY', 89: 'RTNDAY', 90: 'ZAPEXPLN', 91: 'XFERUNIT', 92: 'MOVE', 93: 'MARITAL', 94: 'NUMDEPEND', 95: 'EXEMPT', 96: 'WITHEXTRA', 97: 'VETRANSTAT', 98: 'MAGONLY', 99: 'DDLRFEE', 100: 'DPRCNTFEE', 101: 'DMLGFEE', 102: 'DDLEXP', 103: 'DINSRNCEXP', 104: 'SEX', 105: 'JOBSTATUS', 106: 'EMPCODE1', 107: 'EMPCODE2', 108: 'BOHPASSWRD', 109: 'SECLEVEL', 110: 'STARTTIME', 111: 'ENDTIME', 112: 'PWDCHANGE', 113: 'PENID', 114: 'TEAMSORT', 115: 'TEAMLMTREV', 116: 'ADDRESS3', 117: 'ADDRESS4', 118: 'COUNTY', 119: 'THUMBSCCI', 120: 'WORKPOLID', 121: 'EMPTYPEID', 122: 'THUMBSCLI', 123: 'REMARKS', 124: 'SCHEDSTART', 125: 'SCHEDEND', 126: 'EMPCODE3', 127: 'EMPCODE4', 128: 'EMPCODE5', 129: 'WAIVEMBRK', 130: 'LASTCHPSWD', 131: 'BOHLASTPWD', 132: 'NCFLOGON', 133: 'SSN_ENC', 134: 'EMPLIQCERT', 135: 'EMPLIQEXP', 136: 'MINORXMT', 137: 'BOHHASHPW', 138: 'EXP_ID'}
            self.dict_rec = { v:row[k] for k,v in self.dict_key.items() }
            self.ID = row[0]
            self.OWNERID = row[1]
            self.USERNUMBER = row[2]
            self.EMPLOYEE_NUMBER = row[139]
            self.HOMESITE_NUMBER = row[140]
            """
            self.SEC_NUM = row[3]
            self.SSN = row[4]
            self.SSNTEXT = row[5]
            self.FIRSTNAME = row[6]
            self.MIDDLENAME = row[7]
            self.LASTNAME = row[8]
            self.NICKNAME = row[9]
            self.ADDRESS1 = row[10]
            self.ADDRESS2 = row[11]
            self.CITY = row[12]
            self.STATE = row[13]
            self.ZIPCODE = row[14]
            self.PHONE = row[15]
            self.COUNTRY = row[16]
            self.COUNTRYCDE = row[17]
            self.LOCALEID = row[18]
            self.BIRTHDAY = row[19]
            self.DATEOFHIRE = row[20]
            self.LASTACCESS = row[21]
            self.PASSWORD = row[22]
            self.MAGCARD = row[23]
            self.SECURITY = row[24]
            self.TIPS = row[25]
            self.QWERTY = row[26]
            self.WKTOTMIN = row[27]
            self.WKTOVMIN = row[28]
            self.WKDOVMIN = row[29]
            self.WKTOTPAY = row[30]
            self.WKTOVPAY = row[31]
            self.WKDOVPAY = row[32]
            self.JOBCODE1 = row[33]
            self.JOBCODE2 = row[34]
            self.JOBCODE3 = row[35]
            self.JOBCODE4 = row[36]
            self.JOBCODE5 = row[37]
            self.JOBCODE6 = row[38]
            self.JOBCODE7 = row[39]
            self.JOBCODE8 = row[40]
            self.JOBCODE9 = row[41]
            self.JOBCODE10 = row[42]
            self.PAYRATE1 = row[43]
            self.PAYRATE2 = row[44]
            self.PAYRATE3 = row[45]
            self.PAYRATE4 = row[46]
            self.PAYRATE5 = row[47]
            self.PAYRATE6 = row[48]
            self.PAYRATE7 = row[49]
            self.PAYRATE8 = row[50]
            self.PAYRATE9 = row[51]
            self.PAYRATE10 = row[52]
            self.ACCESS1 = row[53]
            self.ACCESS2 = row[54]
            self.ACCESS3 = row[55]
            self.ACCESS4 = row[56]
            self.ACCESS5 = row[57]
            self.ACCESS6 = row[58]
            self.ACCESS7 = row[59]
            self.ACCESS8 = row[60]
            self.ACCESS9 = row[61]
            self.ACCESS10 = row[62]
            self.SKILL1 = row[63]
            self.SKILL2 = row[64]
            self.SKILL3 = row[65]
            self.SKILL4 = row[66]
            self.SKILL5 = row[67]
            self.SKILL6 = row[68]
            self.SKILL7 = row[69]
            self.SKILL8 = row[70]
            self.SKILL9 = row[71]
            self.SKILL10 = row[72]
            self.PREF1 = row[73]
            self.PREF2 = row[74]
            self.PREF3 = row[75]
            self.PREF4 = row[76]
            self.PREF5 = row[77]
            self.PREF6 = row[78]
            self.PREF7 = row[79]
            self.PREF8 = row[80]
            self.PREF9 = row[81]
            self.PREF10 = row[82]
            self.MEALS = row[83]
            self.MEALPCNT = row[84]
            self.TERMINATED = row[85]
            self.ZAPID = row[86]
            self.REHIRE = row[87]
            self.LASTDAY = row[88]
            self.RTNDAY = row[89]
            self.ZAPEXPLN = row[90]
            self.XFERUNIT = row[91]
            self.MOVE = row[92]
            self.MARITAL = row[93]
            self.NUMDEPEND = row[94]
            self.EXEMPT = row[95]
            self.WITHEXTRA = row[96]
            self.VETRANSTAT = row[97]
            self.MAGONLY = row[98]
            self.DDLRFEE = row[99]
            self.DPRCNTFEE = row[100]
            self.DMLGFEE = row[101]
            self.DDLEXP =row[102]
            self.DINSRNCEXP = row[103]
            self.SEX = row[104]
            self.JOBSTATUS = row[105]
            self.EMPCODE1 = row[106]
            self.EMPCODE2 = row[107]
            self.BOHPASSWRD = row[108]
            self.SECLEVEL = row[109]
            self.STARTTIME = row[110]
            self.ENDTIME = row[111]
            self.PWDCHANGE = row[112]
            self.PENID = row[113]
            self.TEAMSORT = row[114]
            self.TEAMLMTREV = row[115]
            self.ADDRESS3 = row[116]
            self.ADDRESS4 = row[117]
            self.COUNTY = row[118]
            self.THUMBSCCI = row[119]
            self.WORKPOLID = row[120]
            self.EMPTYPEID = row[121]
            self.THUMBSCLI = row[122]
            self.REMARKS = row[123]
            self.SCHEDSTART = row[124]
            self.SCHEDEND = row[125]
            self.EMPCODE3 = row[126]
            self.EMPCODE4 = row[127]
            self.EMPCODE5 = row[128]
            self.WAIVEMBRK = row[129]
            self.LASTCHPSWD = row[130]
            self.BOHLASTPWD = row[131]
            self.NCFLOGON = row[132]
            self.SSN_ENC = row[133]
            self.EMPLIQCERT = row[134]
            self.EMPLIQEXP = row[135]
            self.MINORXMT = row[136]
            self.BOHHASHPW = row[137]
            self.EXP_ID = row[138]
            """
    def __getitem__(self, key):
        """Return value by field name or field index."""
        if isinstance(key, int):
            # integer index of the field
            return self.fields[key]
        # assuming string field name
        return self.fields[self.header.index_of_field_name(key)]


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
    def add_record_as_data(self,_record):
        self.__dict__.update(_record.__dict__)
    def add_dict_as_data(self,_dict):
        self.__dict__.update(_dict)
    def add_record_as_attr(self,_record):
        self.record = _record