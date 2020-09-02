import pyperclip
new_s=""
with open("/Users/winnie26/Documents/SMS_script/password.txt") as f:
    lines = f.read().splitlines()
    if not lines:
        print("**TEXT YOURSELF NEW PASSWORD!**") 
        exit()
    to_list = lines[0].split()
    res = to_list.pop(0)
    pyperclip.copy(res)
    new_s = " ".join(to_list)
with open("/Users/winnie26/Documents/SMS_script/password.txt",'w') as writer:
    writer.write(new_s)
exit()
