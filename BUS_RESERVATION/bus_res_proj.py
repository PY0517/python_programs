import copy
seats={'A1':True,'A2':True,'A3':True,'A4':True,
       'B1':True,'B2':True,'B3':True,'B4':True,
       'C1':True,'C2':True,'C3':True,'C4':True,
       'D1':True,'D2':True,'D3':True,'D4':True,
       'E1':True,'E2':True,'E3':True,'E4':True,
       'F1':True,'F2':True,'F3':True,'F4':True}
services={101: ['hyd', 'vij',14.00,22.00,300,copy.deepcopy(seats)],
          102: ['kkd', 'viz',10.00,2.00,250,copy.deepcopy(seats)],
          103: ['ynm', 'chn',23.00,23.00,200,copy.deepcopy(seats)],
          104: ['blr', 'hyd',10.00,2.00,150,copy.deepcopy(seats)]}
print(services)
service_no=105
def create_services(service):
    global service_no
    source=input("enter source city")
    destination=input("enter destination city :")
    start_time=input("Enter the start time :")
    end_time=input("Enter the end time :")
    kml=input("Enter the kilo meters :")
    service[service_no]=[source,destination,start_time,end_time,kml]
    service_no+=1
#create_services(services)
print(services)
def update_services(service):
    num=int(input("enter the service no :"))
    if num in service:
        print(f"source:{service[num][0]}\ndestination:{service[num][1]}")
        n=int(input(f"are you sure to modify {num} details:\n1.confirm\n2.cancel\nchoose the option :"))       
        if n==1:
            service[num][0]=input("Enter the source city :")
            service[num][1]=input("Enter the destination city :")
            service[num][2]=input("Enter the start time :")
            service[num][3]=input("Enter the end time :")
            service[num][4]=input("Enter the kilometers :")

            print("services details modified")
            print(f"modified details in source:{service[num][0]} in destination:{service[num][1]}")
        else:
            return
    else:
        print("invalid service_no")
#update_services(services)
print(services)
seats={'A1':True,'A2':True,'A3':False,'A4':True,
       'B1':True,'B2':False,'B3':True,'B4':True,
       'C1':False,'C2':True,'C3':True,'C4':True,
       'D1':True,'D2':True,'D3':False,'D4':True,
       'E1':False,'E2':True,'E3':True,'E4':True,
       'F1':True,'F2':True,'F3':True,'F4':False}
def bus_seats(coll):
    available=[]
    unavailable=[]
    for i in coll:
        if coll[i]==True:
            available+=[i]
        else:
            unavailable+=[i]
    return(available,unavailable)
res=bus_seats(seats)
print("Total seats",len(seats))
print("available seats",res[0])
print("unavailable seats",res[1])
print("count available seats",len(res[0]))
print("count unavailable seats",len(res[1]))

def display_all_service(service):
    for i in service.items():
        seats=bus_seats(i[1][-1])
        print(str(i[0]).center(20),
                  i[i][0].center(20),
                  i[i][1].center(20),
                  str(i[i][2]).center(20),
                  str(i[i][3]).center(20),
                  str(i[i][4]).center(20),
                  str(len(services[i][-1])).center(20),
                  str(len(seats[0])).center(20),
                  str(len(seats[1])).center(20))
def display_service_no(service,ele):
    for i in service:
        if ele==i:
            seats=bus_seats(services[i][-1])
            print(str(i).center(20),
                  services[i][0].center(20),
                  services[i][1].center(20),
                  str(services[i][2]).center(20),
                  str(services[i][3]).center(20),
                  str(services[i][4]).center(20),
                  str(len(services[i][-1])).center(20),
                  str(len(seats[0])).center(20),
                  str(len(seats[1])).center(20))
def display_service_destination(service,ele):
    for i in services:
        if ele.upper()==services[i][0].upper():
            seats=bus_seats(service[i][-1])
            print(str(i).center(20),
                  services[i][0].center(20),
                  services[i][1].center(20),
                  str(services[i][2]).center(20),
                  str(services[i][3]).center(20),
                  str(services[i][4]).center(20),
                  str(len(services[i][-1])).center(20),
                  str(len(seats[0])).center(20),
                  str(len(seats[1])).center(20))
def display_service_source(service,ele):
    for i in services:
        if ele.upper()==services[i][1].upper():
            seats=bus_seats(service[i][-1])
            print(str(i).center(20),
                  services[i][0].center(20),
                  services[i][1].center(20),
                  str(services[i][2]).center(20),
                  str(services[i][3]).center(20),
                  str(services[i][4]).center(20),
                  str(len(services[i][-1])).center(20),
                  str(len(seats[0])).center(20),
                  str(len(seats[1])).center(20))
def display_service_both(service,ele,ele1):
    for i in services:
        if ele.upper()==services[i][0].upper() and ele1.upper()==services[i][1].upper():
            seats=bus_seats(service[i][-1])
            print(str(i).center(20),
                  services[i][0].center(20),
                  services[i][1].center(20),
                  str(services[i][2]).center(20),
                  str(services[i][3]).center(20),
                  str(services[i][4]).center(20),
                  str(len(services[i][-1])).center(20),
                  str(len(seats[0])).center(20),
                  str(len(seats[1])).center(20))
def display_services():
    print("service no".center(20),"source".center(20),"destination".center(20),"start time ".center(20),"End time".center(20),
"kilometers".center(20),"Total seats".center(20),"available seats".center(20),"unavailable seats".center(20))
    print("-------".center(20),"------".center(20),"-------".center(20),"-------".center(20),"------".center(20),
"-------".center(20),"-------".center(20),"------".center(20),"-------".center(20))
    n=int(input("Choose the option :\n1.service_no\n2.source\n3.Destinnation\n4.Source and Destination\n5.All services\n Enter :"))
    match n:
        case 1:
            ele=int(input("Enter the service number :"))
            display_service_no(services,ele=ele)
        case 2:
            ele=input("Enter the source city :")
            display_service_source(services,ele=ele)
        case 3:
            ele=input("Enter the Destination city :")
            display_service_destination(services,ele=ele)
        case 4:
            ele=input("Enter the source city :")
            ele1=input("Enter the destination city :")
            display_service_both(services,ele=ele,ele1=ele1)
        
        case _:
            display_all_service(services)
#display_services()

print(services)
for i in services:
    print(i,services[i])

import copy
date_wise_services={}

def seat_pattern(seats):
    res=list(seats)
    count=0
    for i in range(0,len(seats)//2):
        for j in range(0,4):
            if seats[res[count]]!=True:
                print(f"@{seats[res[count]][-1]['gender'][0]}".center(8),end=" ")
            else:
                print(res[count].center(8),end=" ")
            count+=1
        print()
# seat_pattern(seats)

def check_services(date1):
    global bus
    ser=int(input('enter the serice no:'))
    if ser in date_wise_services[date1]:
        #print("service no".center(20),"source".center(20),"destination".center(20),"start time ".center(20),"End time".center(20),
        #"price".center(20),"Total seats".center(20))
        #print("-------".center(20),"------".center(20),"-------".center(20),"-------".center(20),"------".center(20),
        # "-------".center(20),"-------".center(20),"------".center(20),"-------".center(20))
        bus=date_wise_services[date1][ser]
        print(str(ser).center(20),
                  bus[0].center(20),
                  bus[1].center(20),
                  str(bus[2]).center(20),
                  str(bus[3]).center(20),
                  str(bus[4]*2).center(20),
                  str(len(bus[5])).center(20))
    else:
        print("service is not Available")
        return check_services(date1)
        
def booking(seats):
    n=int(input("enter the seats:"))
    l=[]
    for i in range(0,n):
        seat_no=input("enter thr seat no")
        if seats[seat_no]!=True:
            print(f"Your {seat_no} selected seat already booked")
            print('Reenter')
            return()
        else:
            l+=[seat_no]
    d={}
    for i in l:
        print("your seat no:",i)
        name=input("enter the name:")
        age=input("enter the age:")
        gender=input("enter the gender:")
        if int(i[-1])%2==0 and seats[i[0]+str(int(i[-1])-1)]!=True:
            if seats[i[0]+str(int(i[-1])-1)][1]['gender'].upper()==gender.upper():
                d[i]=(False,{'name':name,'age':age,'gender':gender})
            else:
                print(i,f"seats should be {seats[i[0]+str(int(i[-1])-1)][1]['gender']}")
                return booking()
        elif int(i[-1])%2!=0 and seats[i[0]+str(int(i[-1])+1)]!=True:
            if seats[i[0]+str(int(i[-1])+1)][1]['gender'].upper()==gender.upper():
                d[i]=(False,{'name':name,'age':age,'gender':gender})
            else:
                print(i,f"seats should be {seats[i[0]+str(int(i[-1])+1)][1]['gender']}")
                return booking()
        else:
            d[i]=(False,{'name':name,'age':age,'gender':gender})
    return d
# booking(seats)     

bank_info={"7788994456@YBL":{'name':'Ramu','pin':2255,'balance':9000,'phone':9988774455},'7788994455@YBL':{'name':'Raju','pin':7895,'balance':9000,'phone':9988774411}}
def payment_mode(price):
    userid=input('enter the UPI ID:').upper()
    if userid in bank_info:
        print(f"Dear{bank_info[userid]['name']}")
        pin=int(input('enter the pin:'))
        if pin==bank_info[userid]['pin']:
            if bank_info[userid]['balance']>price:
                print('PAYMNET IS SUCCESS')
                bank_info[userid]['balance']-=price
                return True
            else:
                print('INSUFFICIENT BALANCE')
                return payment_mode(price)
        else:
            print('INVALID PIN NO')
            return payment_mode(price)
    else:
        print('INVALID UPI ID')
        return payment_mode(price)

def search_buses(service_no):
    ele=input("enter the Source city:")
    ele1=input("enter the destination city:")
    date1=input("enter the date:")
    if date1 not in date_wise_services:
        date_wise_services[date1]=copy.deepcopy(services)
    print("service no".center(20),"source".center(20),"destination".center(20),"start time ".center(20),"End time".center(20),
        "price".center(20),"Total seats".center(20),"Available seats".center(20))
    
    print("-------".center(20),"------".center(20),"-------".center(20),"-------".center(20),"------".center(20),
        "-------".center(20),"-------".center(20),"------".center(20))
    global bus
    for i in date_wise_services[date1]:
        if services[i][0].upper()==ele.upper() and services[i][1]==ele1.upper():
            bus=services[i]
            print(str(i).center(20),
                  bus[0].center(20),
                  bus[1].center(20),
                  str(bus[2]).center(20),
                  str(bus[3]).center(20),
                  str(bus[4]*2).center(20),
                  str(len(bus[5])).center(20),
                  str(len(bus_seats(bus[5])[0])).center(20),
                  str(len(bus_seats(bus[5])[1])).center(20))
    service_no=check_services(date1)
    print(service_no)
    res=booking(bus[5])
    price=len(res)*(bus[4]*2)


    print("BOOKING INFO".center(30),"*")
    print("Person Name".center(15),"Age".center(10),"Gender".center(10),"Seat no".center(10))
    for k in res:
        print(res[k][-1]['name'].center(15),str(res[k][-1]['age']).center(10),str(res[k][-1]['gender']).center(10),k.center(10))
    print("*"*30)
    print("Total Ticket Price:",price)
    total_price=price+100
    print("Total Price + Tax:",total_price)
    print("*"*30)
    n=int(input("Are you sure to book the seats:\n1.confirm\n2.cancel\nchoose the option:"))
    if n==1:
        # print(date_wise_services[date1][service_no])
        if payment_mode(total_price)==True:
            date_wise_services[date1][service_no]=res
    print(date_wise_services[date1][service_no])
search_buses(service_no)

# def bus_services_details():
#     for j in date_wise_services:
#         print(j)
#         for i in date_wise_services[j]:
#             print(i,date_wise_services[j][i])
# search_buses(service_no)