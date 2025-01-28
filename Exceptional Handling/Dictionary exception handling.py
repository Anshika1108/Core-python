list = {"Name":"Anshika","Age":21,"Place":"Indore"}
k = input("Enter key to search :")
d = list.keys()
try:
    v=list[k]
    print("key is present")
except Exception:
    print("key not found")