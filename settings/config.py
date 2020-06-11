from tools.ConfigParser import ConfigParser_manager as CM
from system.path import getpath
import os
from termcolor import cprint
from settings.settings import bot as bt
from settings.settings import interaction_setting as its
from settings.settings import update_bot

config_keys = ['-config','-settings']
conf_path = os.path.join(getpath(__file__),'settings.conf')

yes = ['yes','y']

class Config:
    obj = CM()
    lt = ['Bot','Interaction','Competitive Programming']
    cp = [
        'Coder Name',
        'Competitive companion port number',
        'Parse Problem with template',
        'Template Path',
        'Compiler'
    ]
    def change_gender(self):
        pt = '-'*22 + 'Gender Change' +'-'*22
        cprint(pt,'magenta')
        print()
        cprint(f" Current gender : {bt['gender']}",'yellow')
        cprint(" Enter new gender : ",'cyan',end='')
        new_name = input()
        cprint(" Do you want to update?(Y/N) : ",'cyan',end='')
        confirm = input()
        if confirm.lower() in yes:
            section = 'bot'
            x = self.obj.read(conf_path,section)
            x['gender'] = new_name
            self.obj.update(conf_path,x,section)
            bt['gender'] = new_name
            update_bot(bt)
            cprint("Gender Changed successfully.",'green')
        else :
            cprint("Cancelled.",'red')


    def change_name(self):
        pt = '-'*22 + 'Name Change' +'-'*22
        cprint(pt,'magenta')
        print()
        cprint(f" Current Name : {bt['name']}",'yellow')
        cprint(" Enter new name : ",'cyan',end='')
        new_name = input()
        cprint(" Do you want to update?(Y/N) : ",'cyan',end='')
        confirm = input()
        if confirm.lower() in yes:
            section = 'bot'
            x = self.obj.read(conf_path,section)
            x['name'] = new_name
            self.obj.update(conf_path,x,section)
            bt['name'] = new_name
            update_bot(bt)
            cprint("Name Changed successfully.",'green')
        else :
            cprint("Cancelled.",'red')

    def change_boss(self):
        
        pt = '-'*22 + 'Boss Change' +'-'*22
        cprint(pt,'magenta')
        print()
        cprint(f" Current Boss : {bt['boss']}",'yellow')
        cprint(" Enter new boss : ",'cyan',end='')
        new_name = input()
        cprint(" Do you want to update?(Y/N) : ",'cyan',end='')
        confirm = input()
        if confirm.lower() in yes:
            section = 'bot'
            x = self.obj.read(conf_path,section)
            x['boss'] = new_name
            self.obj.update(conf_path,x,section)
            bt['boss'] = new_name
            update_bot(bt)
            cprint("Boss Changed successfully.",'green')
        else :
            cprint("Cancelled.",'red')

    def change_voice_engine(self):
        pt = '-'*22 + 'Voice Engine Change' +'-'*22
        cprint(pt,'magenta')
        print()
        cprint(f" Current voice engine : {bt['boss']}",'yellow')
        

    def bot(self,no):
        bot = [
            'Name',
            'Gender',
            'Boss',
            'Voice_engine'
        ]
        pt = '-'*22 + self.lt[no] +'-'*22
        cprint(pt,'magenta')
        cprint(" Select the index to change,",'yellow')
        
        print()
        # print(bt)
        for i,w in enumerate(bot):
            cprint(f'  {i+1}) {w} : {bt[w.lower()]}','blue')
        cprint('  0) Cancel','red')
        print()
        ok = True

        while ok:
            ok = False
            cprint(" Enter the index number : ",'cyan',end='')
            no = int(input())
            if no == 0:
                cprint(" Operation cancelled.",'red')
                return
            elif no == 1:
                cprint(f' You have selected {bot[no-1]} .','yellow')
                self.change_name()
            elif no == 2:
                cprint(f' You have selected {bot[no-1]} .','yellow')
                self.change_gender()
            elif no == 3:
                cprint(f' You have selected {bot[no-1]} .','yellow')
                self.change_boss()
            elif no == 4:
                cprint(" Sorry temporary this option is unavailable.",'red')
                ok = True
                continue
                cprint(f' You have selected {bot[no-1]} .','yellow')
                self.change_voice_engine()
            else :
                ok = True
                cprint(" You have selected wrong index. Please try again.",'red')



    def Interaction(self,no):

        options = [
            'voice_reply',
            'text_reply',
            'voice_read_voice_reply',
            'text_read'
        ]
        pt = '-'*22 + self.lt[no] +'-'*22
        cprint(pt,'magenta')
        cprint(" Select the index to change,",'yellow')
        
        print()
        
        for i,w in enumerate(options):
            cprint(f'  {i+1}) {w} : {its[w.lower()]}','blue')
        cprint('  0) Cancel','red')
        print()
        ok = True

        while ok:
            ok = False
            cprint(" Enter the index number : ",'cyan',end='')
            no = int(input())
            if no == 0:
                cprint(" Operation cancelled.",'red')
                return
            elif no == 1:
                cprint(f' You have selected {options[no-1]} .','yellow')
                key = options[no-1]
                if its[key] :
                    cprint(f' Do you want to turn {key} to False?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = False
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'False'
                        self.obj.update(conf_path,x,section)

                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')
                else :
                    cprint(f' Do you want to turn {key} to True?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = True
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'True'
                        self.obj.update(conf_path,x,section)

                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')


            elif no == 2:
                cprint(f' You have selected {options[no-1]} .','yellow')
                key = options[no-1]
                if its[key] :
                    cprint(f' Do you want to turn {key} to False?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = False
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'False'
                        self.obj.update(conf_path,x,section)
                        
                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')
                else :
                    cprint(f' Do you want to turn {key} to True?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = True
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'True'
                        self.obj.update(conf_path,x,section)

                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')

            elif no == 3:
                cprint(f' You have selected {options[no-1]} .','yellow')
                key = options[no-1]
                if its[key] :
                    cprint(f' Do you want to turn {key} to False?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = False
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'False'
                        self.obj.update(conf_path,x,section)
                        
                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')
                else :
                    cprint(f' Do you want to turn {key} to True?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = True
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'True'
                        self.obj.update(conf_path,x,section)

                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')

            elif no == 4:
                cprint(f' You have selected {options[no-1]} .','yellow')
                key = options[no-1]
                if its[key] :
                    cprint(f' Do you want to turn {key} to False?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = False
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'False'
                        self.obj.update(conf_path,x,section)
                        
                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')
                else :
                    cprint(f' Do you want to turn {key} to True?(Y/N) : ','cyan',end='')
                    confirm = input()
                    if confirm.lower() in yes:
                        its[key] = True
                        section = 'interaction_setting'
                        x = self.obj.read(conf_path,section)
                        x[key] = 'True'
                        self.obj.update(conf_path,x,section)

                        cprint(" Successfully updated.",'green')
                    else :
                        cprint("Cancelled.",'red')

            else :
                ok = True
                cprint(" You have selected wrong index. Please try again.",'red')

    def competitive_companion(self):
        try :
            from settings.compiler import competitive_companion_port as ccp, update_ccp
            pt = '-'*22 + 'Competitive Companion' +'-'*22
            cprint(pt,'magenta')
            print()

            cprint(" Current port number : " + str(ccp),'yellow')

            cprint('  1) Change port.','blue')
            cprint('  0) Back.','red')

            ok = True
            while ok:
                ok = False
                cprint(' Enter the index number : ','cyan',end='')
                no = int(input())
                if no == 0:
                    cprint(" Going back.",'red')
                    self.competitve_programming()
                elif no == 1:
                    print()
                    cprint(" Enter new port number(must be integer) : ",'cyan',end='')
                    port = int(input())
                    # ccp = port
                    update_ccp(port)
                    section = 'cp'
                    x = self.obj.read(conf_path,section)
                    x['competitive_companion_port'] = str(port)
                    self.obj.update(conf_path,x,section)
                    cprint(' Competitive companion port updated succussfully.','green')
                    self.competitive_companion()
                else:
                    cprint(" You have choosen wrong index.",'red')
                    ok = True
        except Exception as e:
            cprint(e,'red')

    def temp_path(self):
        try :
            cprint(" Temporary unvailable.",'red')
        except Exception as e:
            cprint(e,'red')

    def compiler_option(self):
        try :
            cprint(" Temporary unvailable.",'red')
        except Exception as e:
            cprint(e,'red')


    def competitve_programming(self,no=2):
        optinos = [
            'Competitive Companion.',
            'Template Path.',
            'Compiler'
        ]

        pt = '-'*22 + self.lt[no] +'-'*22
        cprint(pt,'magenta')
        print()
        cprint(" All the available settings are given below,",'yellow')
        
        print()
        # print(bt)
        for i,w in enumerate(optinos):
            cprint(f'  {i+1}) {w}','blue')
        cprint('  0) Cancel','red')
        print()
        ok = True

        while ok:
            ok = False
            cprint(" Enter the index number : ",'cyan',end='')
            no = int(input())
            if no == 0:
                cprint(" Operation cancelled.",'red')
                return
            elif no == 1:
                cprint(f' You have selected {optinos[no-1]} .','yellow')
                self.competitive_companion()
            elif no == 2:
                cprint(f' You have selected {optinos[no-1]} .','yellow')
                self.temp_path()
            elif no == 3:
                cprint(f' You have selected {optinos[no-1]} .','yellow')
                self.compiler_option()
            else :
                ok = True
                cprint(" You have selected wrong index. Please try again.",'red')




    def config_list(self):
        not_done = True
        while not_done:

            pt = '-'*22 + 'Config'+'-'*22
            cprint(pt,'magenta')
            print()
            cprint(" All the available settings are given below,",'yellow')
            print()
            for i,w in enumerate(self.lt):
                cprint(f'  {i+1}) {w}','blue')
            cprint('  0) Exit','red')
            print()
            ok = True
            while ok:
                ok = False
                cprint(" Enter the index number : ",'cyan',end='')
                no = int(input())
                if no == 0:
                    cprint(" Exiting.",'red')
                    cprint(" For some setting you might need to restart.",'yellow')
                    not_done = False
                elif no == 1:
                    cprint(f' You have selected {self.lt[no-1]} .','yellow')
                    self.bot(no-1)
                elif no == 2:
                    cprint(f' You have selected {self.lt[no-1]} .','yellow')
                    self.Interaction(no-1)
                elif no == 3:
                    cprint(f' You have selected {self.lt[no-1]} .','yellow')
                    self.competitve_programming(no-1)
                else :
                    ok = True
                    cprint(" You have selected wrong index. Please try again.",'red')




def if_config_type(msg):
    if msg in config_keys:
        obj = Config()
        obj.config_list()
        return True
    else:
        return False