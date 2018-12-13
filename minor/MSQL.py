import pyodbc
import minor.Configure

class SqlDb(object):

    def __init__(self, server=None,database=None,uid=None,password=None):

        self.server = server
        self.database = database
        self.uid = uid
        self.password = password
        #self.conn = self.createConn()


    def createConn(self):
        try:
            odbc_driver = ['ODBC', 'SQL Server Native', 'SQL Native', 'SQL Server']
            driver = next(filter(lambda source: any(filter(lambda prefix: source.startswith(prefix),odbc_driver)), pyodbc.drivers()))
            cnxn = pyodbc.connect("Driver={"+ driver +"};"
                                  "Server="+ self.server + ";"
                                  "Database="+ self.database + ";"
                                  "UID=" + self.uid+ ";"
                                  "PWD=" + self.password+ ";")
            return cnxn
        except (pyodbc.OperationalError) as e:
            minor.Configure.logger.info("Error {0}".format(str(e, encoding = 'utf-8')))
            return None

    def querySQL(self,querySQL,conn):
        if conn is not None:
            cursor = conn.cursor()
            return cursor.execute(querySQL)
        else:
            return None

    def getEmpData(self,conn,siteNumber):
        query = "select EmployeeID as ID ,0 as OWNERID ,EmployeeID as USERNUMBER ,0 as SEC_NUM \
        ,999999999 as SSN ,999999999 as SSNTEXT ,FirstName as FIRSTNAME ,MiddleName as MIDDLENAME \
        ,LastName as LASTNAME ,FirstName as NICKNAME ,Address1 as ADDRESS1 ,Address2 as ADDRESS2 \
        ,City as CITY ,'' as STATE ,'' as ZIPCODE ,isnull(Phone,'') as PHONE ,isnull(Country,'') as COUNTRY \
        ,0 as COUNTRYCDE ,0 as LOCALEID ,convert(varchar,birthdate,112) as BIRTHDAY ,convert(varchar,HireDate,112) as DATEOFHIRE \
        ,'' as LASTACCESS ,'' as PASSWORD ,'' as MAGCARD ,0 as SECURITY ,0.00 as TIPS ,'N' as QWERTY \
        ,0 as WKTOTMIN ,0 as WKTOVMIN ,0 as WKDOVMIN , 0.00 as WKTOTPAY ,0.00 as WKTOVPAY ,0.00 as WKDOVPAY \
        ,0 as JOBCODE1 ,0 as JOBCODE2 ,0 as JOBCODE3 ,0 as JOBCODE4 ,0 as JOBCODE5 ,0 as JOBCODE6 ,0 as JOBCODE7 ,0 as JOBCODE8 ,0 as JOBCODE9 ,0 as JOBCODE10 \
        ,0.00 as PAYRATE1 ,0.00 as PAYRATE2 ,0.00 as PAYRATE3 ,0.00 as PAYRATE4 ,0.00 as PAYRATE5 ,0.00 as PAYRATE6 ,0.00 as PAYRATE7 ,0.00 as PAYRATE8 ,0.00 as PAYRATE9 ,0.00 as PAYRATE10  \
        ,0 as ACCESS1 ,0 as ACCESS2 ,0 as ACCESS3 ,0 as ACCESS4 ,0 as ACCESS5 ,0 as ACCESS6 ,0 as ACCESS7 ,0 as ACCESS8 ,0 as ACCESS9 ,0 as ACCESS10  \
        ,0 as SKILL1 ,0 as SKILL2 ,0 as SKILL3 ,0 as SKILL4 ,0 as SKILL5 ,0 as SKILL6 ,0 as SKILL7 ,0 as SKILL8 ,0 as SKILL9 ,0 as SKILL10 \
        ,0 as PREF1 ,0 as PREF2 ,0 as PREF3 ,0 as PREF4 ,0 as PREF5 ,0 as PREF6 ,0 as PREF7 ,0 as PREF8 ,0 as PREF9 ,0 as PREF10 \
        ,'N' as MEALS ,0 as MEALPCNT ,'N' as TERMINATED ,0 as ZAPID ,'N' as REHIRE \
        ,'' as LASTDAY ,'' as RTNDAY ,'' as ZAPEXPLN \
        ,0 as XFERUNIT ,'N' as MOVE ,0 as MARITAL ,0 as NUMDEPEND ,'N' as EXEMPT ,0.00 as WITHEXTRA ,0 as VETRANSTAT ,'N' as MAGONLY \
        ,0.00 as DDLRFEE ,0.00000 as DPRCNTFEE ,0.00 as DMLGFEE ,'' as DDLEXP ,'' as DINSRNCEXP \
        ,case Gender when 0 then 'N' else 'Y' end as SEX \
        ,Salaried as JOBSTATUS \
        ,isnull(CustomField1,'') as EMPCODE1 \
        ,isnull(CustomField2,'') as EMPCODE2 \
        ,'' as BOHPASSWRD \
        ,0 as SECLEVEL \
        ,'00:00:' as STARTTIME ,'00:00:' as ENDTIME ,'' as PWDCHANGE ,0 as PENID ,0 as TEAMSORT ,'N' as TEAMLMTREV \
        ,'' as ADDRESS3 ,'' as ADDRESS4 ,'' as COUNTY \
        ,'Y' as THUMBSCCI ,0 as WORKPOLID ,0 as EMPTYPEID ,'Y' as THUMBSCLI \
        ,'' as REMARKS ,'' as SCHEDSTART ,'' as SCHEDEND ,'' as EMPCODE3 ,'' as EMPCODE4 ,'' as EMPCODE5 \
        ,'N' as WAIVEMBRK ,0 as LASTCHPSWD ,0 as BOHLASTPWD ,0 as NCFLOGON \
        ,'' as SSN_ENC ,'' as EMPLIQCERT ,'' as EMPLIQEXP ,0 as MINORXMT ,'' as BOHHASHPW ,'' as EXP_ID \
        ,employeeNumber as EMPLOYEENUMBER,homesite as HOMESITE \
        from employees \
        where homesite = (select siteNumber from sites where sitename like '"+siteNumber+"%')  order by EmployeeID"

        if conn is not None:
            cursor = conn.cursor()
            return cursor.execute(query)
        else:
            return None

    def getEmpProperty(self,siteNumber="",empNumber="",conn=None):
        query = "SELECT  jr.SiteNumber,emp.EmployeeID,jr.JobNumber,jobs.JobID,jr.Rate,cast(jr.PayReasonNumber as smallint) as PayReasonNumber,jr.PrimaryJob,jr.Sequence,Jobs.JobName,RIGHT(sp.StringValue,1) as StringValue \
                FROM SiteEmployeeJobRates jr \
                INNER JOIN Jobs ON Jobs.JobNumber = jr.JobNumber \
                INNER JOIN Employees emp ON emp.EmployeeNumber = jr.EmployeeNumber \
                Cross Apply SiteSpecificJobProperties(1442,jr.SiteNumber,jr.JobNumber, '4', 0) as sp \
                WHERE jr.employeeNumber = "+str(empNumber)+" and jr.SiteNumber = "+str(siteNumber)+" and jr.StartDate <= getDate()  AND ( jr.EndDate IS NULL) \
                AND LEFT(Jobs.JobName,2) NOT IN ('T0', 'T1', 'T2', 'T3', 'T4', \
                                                 'T5', 'T6', 'T7', 'T8', 'T9', \
                                                 'U0', 'U1', 'U2', 'U3', 'U4', \
                                                 'U5', 'U6', 'U7', 'U8', 'U9', \
                                                 'V0', 'V1', 'V2', 'V3', 'V4', \
                                                 'V5', 'V6', 'V7', 'V8', 'V9') \
                 order by jr.PrimaryJob desc,jr.Sequence asc "
        #minor.Configure.logger.info(query)
        if conn is not None:
            cursorProp = conn.cursor()
            return cursorProp.execute(query)
        else:
            return None

    def getStatus(self,siteNumber="",empNumber="",conn=None):
        query ="select status from siteemployees where employeeNumber="+str(siteNumber)+" and siteNumber ="+str(siteNumber)+" and status in (0,1)"
        #minor.Configure.logger.info(query)
        if conn is not None:
            cursor = conn.cursor()
            return cursor.execute(query)
        else:
            return None