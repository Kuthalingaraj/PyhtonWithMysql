import mysql.connector;
from tabulate import tabulate;

con = mysql.connector.connect(
    host="localhost",user="root",password = "admin",database = "mpy"
);


def insert(name,age,place):
    res = con.cursor();
    sql = "insert into details(ename,age,place)values(%s,%s,%s)";
    user=(name,age,place);
    res.execute(sql,user);
    #important one insert update delete confirm commit a connect if not commit does not affect a database
    con.commit();
    print("Data Insert Successfully:");

def update(name,age,place,id):
    res = con.cursor();
    sql = "update details set ename = %s,age = %s,place = %s where id=%s";
    user=(name,age,place,id);
    res.execute(sql,user);
    #important one insert update delete confirm commit a connect if not commit does not affect a database
    con.commit();
    print("Data Insert Successfully:");

def update_name(name,id):
    res = con.cursor();
    
    sql = "update details set ename = %s where id = %s";
    user = (name,id);
    res.execute(sql,user);
    con.commit();
    print("Update Name Successfully");

def update_Age(age,id):
    res = con.cursor();
    
    sql = "update details set age = %s where id = %s";
    user = (age,id);
    res.execute(sql,user);
    con.commit();
    print("Update Age Successfully");



def update_Place(place,id):
    res = con.cursor();
    
    sql = "update details set place = %s where id = %s";
    user = (place,id);
    res.execute(sql,user);
    con.commit();
    print("Update Place Successfully");

def retrive():
    
    
    res = con.cursor();#cursor means our python & mysql connected wire to pass the data from py to mysql and mysql to py
    sql="Select id,ename,age,place from details";
    res.execute(sql);
    result = res.fetchall();
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]));


def delete(id):
    res = con.cursor();
    sql = "delete from details where id=%s";
    user=(id,);
    res.execute(sql,user);
    #important one insert update delete confirm commit a connect if not commit does not affect a database
    con.commit();
    print("Data Delete Successfully:");

while(True):
    print("1.\tInsert Data");
    print("2.\tUpate Data");
    print("3.\tRetrive Data");
    print("4.\tDelete Data");
    print("5.\tExit");
    
    choice = int(input("Enter Your Choice:\t"));
    if choice == 1:
        name = input("Enter Your Name:\t");
        age = int(input("Enter Your Age:\t"));
        place = input("Enter Your Place\t");
        insert(name,age,place);
    elif choice == 2:
        retrive();
       
        print("1.\tUpdate Name:");
        print("2.\tUpdate Age:");
        print("3.\tUpdate Place");
        print("4.\tUpdate All Records")
        c = int(input("Enter the Choice:\t"));
        if c== 1:
            retrive();
            id = input("Enter the Id:\t")
            name = input("Enter the Name:\t");
            update_name(name,id)
            retrive();
        elif c==2:
            retrive();
            id = int(input("Enter the ID:\t"));
            age = int(input("Enter the Updated Age:"));
            update_Age(age,id);
            retrive();
        elif c==3:
            retrive();
            id = int(input("Enter the ID:\t"));
            place = input("Enter Your Place:\t");
            update_Place(place,id);
            retrive();
        elif c==4:
            id = input("Enter the Id:\t")
            name = input("Enter Your Name:\t");
            age = int(input("Enter Your Age:\t"));
            place = input("Enter Your Place\t");
            update(name,age,place,id);
    elif choice ==3:
        retrive();
    elif choice == 4:
        id = int(input("Enter the ID:\t"));
        delete(id);
    elif choice == 5:
        break;
else:
    print("Please Enter Valid Selection");
        