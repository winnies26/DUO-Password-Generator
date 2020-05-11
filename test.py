import pyperclip
new_s=""
with open("sms.txt") as f:
    lines = f.read().splitlines()
    if not lines:
        print("**TEXT YOURSELF NEW PASSWORD!**") 
        exit()
    to_list = lines[0].split()
    # print(lines, type(lines))
    res=to_list.pop(0)
    # print(res, to_list)
    pyperclip.copy(res)
    new_s = " ".join(to_list)

with open("sms.txt",'w') as writer:
    writer.write(new_s)
exit()