client = {1:"Rohan",2:"Harry",3:"Hammad",4:"Smruti"}
log ={1:"Exercise",2:"Diet"}
view = {1:"Read",2:"Add"}
x ="*"
def getdate():
    import datetime
    return datetime.datetime.now()
print("\n",x*49)
print("\n",x*11,"Health Management System",x*12)
print("\n",x*49)
print(" Time :             [",getdate(),"]")
print("",x*49)
print(" Select Client Name : ")
print("")
for num,name in client.items():
       print(" [",num ,"] ",name)
name_choose = int(input("\n Choose Name : "))
print("\n")
print("",x*49)
print(" Client Name :",client[name_choose])
print("",x*49)
for num2,name2 in log.items():
    print(" [",num2,"] ",name2)
log_choose = int(input("\n Choose :"))
print("",x*49)
print(" Client Name :",client[name_choose]," [",log[log_choose],"] ")
print("",x*49)
for num3,name3 in view.items():
    print(" [",num3,"] ",name3,"Log")
view_choose = int(input("\n Choose : "))

if view_choose == 2 :
    op = open(client[name_choose]+"_"+log[log_choose]+".txt","a")
    ok = "y"
    while (ok != "n"):
        print("\n")
        print("", x * 49)
        print(" Client Name :", client[name_choose], " [", log[log_choose], "] [", view[view_choose], "]")
        print("", x * 49)
        print(" Write Your",log[log_choose],"in ","[",getdate(),"]")
        write1 = input(" ")
        op.write(" ["+str(getdate())+"] : "+ write1 + "\n")
        print(" Added your ",write1," in your ",log[log_choose],"Database ")
        ok = input(" Add more in your Database ( y or n ): ")
        continue
        f.close()

if view_choose == 1 :
    op = open(client[name_choose] + "_" + log[log_choose] + ".txt")
    print("\n")
    print("", x * 49)
    print(" Client Name :", client[name_choose], " [", log[log_choose], "] [", view[view_choose], "]")
    print("", x * 49)
    content = op.readlines()
    print("")
    for l in content:
        print(l)
    op.close()










