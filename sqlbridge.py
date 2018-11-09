import pymysql
conn = pymysql.connect(host="localhost",user="root",passwd="dbzbloke98",db="Family")
myCursor = conn.cursor()

myCursor.execute("""CREATE TABLE INCOME
(
Source varchar(50),
Amount int
);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Salary',0);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Business',0);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Interest',0);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Capital Gains',0);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Property',0);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Others',0);
""")

myCursor.execute("""CREATE TABLE EXPENDITURE
(
Source varchar(50),
Amount int
);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Electricity',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Society',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Mobile',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('EMI',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Rent',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Grocery',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Housemaid',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Travel',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Others',0);
""")

myCursor.execute("""CREATE TABLE BUDGET
(
DESCRIPTION varchar(50),
Amount int
);
""")
myCursor.execute("""
INSERT INTO BUDGET VALUES('Saving Percentage',0);
""")

myCursor.execute("""CREATE TABLE PERSONAL_DETAILS
(
DESCRIPTION varchar(50),
Entry varchar(40)
);
""")
myCursor.execute("""
INSERT INTO PERSONAL_DETAILS VALUES('Email ID','abc');
""")

myCursor.execute("""CREATE TABLE VIEW_STATS
(
Source varchar(50),
Total_Amount int
);
""")
myCursor.execute("""
INSERT INTO VIEW_STATS VALUES('Total Income',0);
""")
myCursor.execute("""
INSERT INTO VIEW_STATS VALUES('Total Expenditure',0);
""")
myCursor.execute("""
INSERT INTO VIEW_STATS VALUES('Remaining Amount',0);
""")

conn.commit()
conn.close()
