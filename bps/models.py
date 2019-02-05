import pymysql as db 

host = "localhost"
user = "nandu"
password = "password"
database = "pharmacy"
port = 3306

connection = db.connect(host,user,password,database,port)
cursor = connection.cursor()


# 	1. CREATING drug TABLE
Drug = "CREATE TABLE drug(DRUG_ID VARCHAR(10) PRIMARY KEY NOT NULL,NAME TEXT,DOSE_IN_MG INT(4) ,TYPE ENUM('CAPSULE','TBALET','TONIC','OTHER')\
,MRP FLOAT(7,2) UNSIGNED,EXPIRY DATE,COST_PRICE FLOAT(7,2),STOCK INT);"

# 2. CREATING purchase TABLE
Purchase = "CREATE TABLE purchase(PURCHASE_ID INT PRIMARY KEY NOT NULL auto_increment,PURCHASE_DATE DATE);"

# --3. CREATING patient TABLE
Patient = "CREATE TABLE patient(PATIENT_ID INT(10) UNSIGNED PRIMARY KEY NOT NULL ,NAME TEXT,CONTACT_NO INT(10) UNSIGNED,PLACE TEXT);"

# --4. CREATING sale_transaction TABLE
SaleTransaction = "CREATE TABLE sale_transaction(SALE_ID VARCHAR(10) PRIMARY KEY NOT NULL ,SALE_DATE DATE);"

# --5. CREATING drug_manufacturer TABLE
DrugManufacturer = "CREATE TABLE drug_manufacturer(COMPANY_ID VARCHAR(10) PRIMARY KEY NOT NULL,COMPANY_NAME TEXT);"

# --6. CREATING distributor TABLE
Distributor = "CREATE TABLE distributor(DISTRIBUTOR_ID VARCHAR(10) PRIMARY KEY NOT NULL,CONTACT_NO INT(10) UNSIGNED);"

# --7. CREATING manufactures RELATION
Manufactures = "CREATE TABLE manufactures(COMPANY_ID VARCHAR(10) ,DRUG_ID VARCHAR(10));"

# --8. CREATING prescriptions RELATION 
Prescriptions = "CREATE TABLE prescriptions(PATIENT_ID INT(10) UNSIGNED ,DRUG_ID VARCHAR(10) );"

# --9. CREATING supplies RELATION 
Supplies = "CREATE TABLE supplies(PURCHASE_ID INT ,DISTRIBUTOR_ID VARCHAR(10) ,QUANTITY INT);"

# --10. CREATING sells RELATION 
Sells = "CREATE TABLE sells(DRUG_ID VARCHAR(10) ,PATIENT_ID INT(10) UNSIGNED ,SALE_ID VARCHAR(10) );"

tableNames =[Drug,Purchase,Patient,SaleTransaction,DrugManufacturer,Distributor,Manufactures,Prescriptions,Supplies,Sells]
def createTables():
	for tableName in tableNames:
		cursor.execute(tableName)
		connection.commit()
