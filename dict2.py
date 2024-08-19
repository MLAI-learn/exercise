import statistics

stocks={'info':[600,630,620],
        'ril':[1430,1490,1567],
        'mtl':[234,180,160]}

def print_all():
    for stock,price_list in stocks.items():
        avg = statistics.mean(price_list)
        print(f"{stock} ==> {price_list} ==> avg:",round(avg,2))


def add():
    i=input('enter ticker')
    p=input('enter price')
    p=float(p)
    if i in stocks:
        stocks[i].append(p)
    else:
        stocks[i]=[p]
    print_all()


def main():
    op=input('enter operation:print or add:')
    op=op.lower()
    if op=='print':
        print_all()
    elif op=='add':
        add()
    else:
        print('unsupported op:',op)



if __name__=='__main__':
    main()
