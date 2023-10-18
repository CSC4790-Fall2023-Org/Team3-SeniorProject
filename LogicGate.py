def AndGate(b1, b2):
    return b1 and b2

def OrGate(b1, b2):
    return b1 or b2

def XorGate(b1, b2):
    if b1 == b2:
        return False
    else:
        return True
    
def NotGate(b):
    return not b

def BufferGate(b):
    return b

node1 = True
node2 = False
final = AndGate(node1,node2)
print('Node1: ' + str(node1))
print('Node2: ' + str(node2))
print(final)
while True:
    kb = input('Enter a Gate: ')
    if kb == 'and':
        final = AndGate(node1,node2)
        print(final)
    elif kb == 'or':
        final = OrGate(node1,node2)
        print(final)
    else:
        final = XorGate(node1,node2)
        print(final)

