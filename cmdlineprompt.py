import argparse

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--physics",help="phy")
    parser.add_argument("--chemistry",help="che")
    parser.add_argument("--biology",help="bio")
    parser.add_argument("--operation",help='operation',\
                        choices=['total','average'])
    
    args=parser.parse_args()
    print('physics',args.physics)
    print('chemistry',args.chemistry)
    print('biology',args.biology)
    print('operation',args.operation)

    n1=int(args.physics)
    n2=int(args.chemistry)
    n3=int(args.biology)

    total=None
    avg=None
    total=n1+n2+n3

    if args.operation=='total':
        
        print('total',total)
    elif args.operation=='average':
        avg=total/3
        print('avg:',avg)
