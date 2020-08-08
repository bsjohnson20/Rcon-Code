import tkinter as GUI
def KeepLoop():
    NoAnswer=False
    while NoAnswer != True:
        KeepLooping1=input('Do you want to repeat loop?, 1 or 0')
        if KeepLooping1 == '1':
            KeepLooping = True
            return KeepLooping
        elif KeepLooping1=='0':
            KeepLooping=False
            return KeepLooping
def username_quoted():
    username=input('UsernamePlease')
    quotes="'"
    Username=quotes+username+quotes
    return Username
Choice1=input('"1" search premade commands, "2" search code snippets: ')
if Choice1 == '1':
    print('Activating premade command list')
elif Choice1 == '2':
    print('Activating code snippets')
    CodeSnippetsType=input('1 for CBlob@, 2 for CMap, 3 for idk')
    if CodeSnippetsType=='1':
        KeepLooping=True
        while KeepLooping == True:
            KeepLooping=KeepLoop()
            ChoiceCBlob=input('1 for getBlobByplayername, 2 for... : ')
            UsernameReturn=username_quoted()
            if ChoiceCBlob=='1':
                choiceBlobUsername=input('do . then command (1) or assign to variable? (2): ')
                if choiceBlobUsername=='1':
                    print(".getPlayerByUsername("+UsernameReturn+").getBlob()")
                elif choiceBlobUsername=='2':
                    Variable=input('variable pls')
                    print("CBlob@ "+ Variable+"=getPlayerByUsername("+UsernameReturn+").getBlob()")
