india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
a=input('input city 1 ')
b=input('input city 2 ')

if a in india and b in india:
    print('cities are in india')
elif a in pakistan and b in pakistan:
    print('cities are in pakistan')
elif a in bangladesh and b in bangladesh:
    print('cities are in bangladesh')
else:
    print('cant find cities')

