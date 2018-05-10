import json
from os import path,makedirs,system,listdir
from time import sleep
from sys import exit,stdin
from datetime import datetime

def main_menu_ui():

    myacc = account()
    done = False

    while not done:

        print('''
1. LOG IN
2. CREATE ACCOUNT
3. EXIT
            ''')

        idx = int(input('enter menu >>>'))
        system('cls')

        if idx == 1:
            login_success = myacc.login()

            if login_success:
                system('cls')
                post_ui(myacc)
            else:
                print('LOGIN FAILED')
                sleep(1)
                system('cls')

        elif idx == 2:
            myacc.create_account()
        else:
            exit()

def post_ui(acc):

    mypost = post(acc.myid)
    done = False

    while not done:
        print('''
1. WRITE POST
2. READ POST
3. BACK
                ''')
        idx = int(input('enter menu>>>'))
        system('cls')

        if idx == 1:
            mypost.write_post()
        elif idx == 2:
            posts = mypost.get_post()

            if len(posts) == 0:
                print('NO POSTS')
                sleep(1)
                system('cls')
            else:
                for i in range(len(posts)):
                    print(str(i+1)+ '. ' + posts[i])
            
                while True:
                    idx = int(input('WHICH FILE:'))

                    if idx > 0 and idx <= len(posts):
                        mypost.read_post(posts[idx-1])
                        break
                    else:
                        print('ERROR : INDEX OUT OF RANGE!')
        else:
            done = True

    main_menu_ui()

def ensure_dir(file_path):
    '''
    파일이 들어가있어야할 경로가 없으면 만들어 주는 함수

    사용자 정보, 작성글에 대한 정보가 담겨있는 파일이
    들어가는 경로를 만들어 준다
    '''
    directory = path.dirname(file_path)

    if not(path.exists(file_path)):
        makedirs(directory)

class account():

    def __init__(self):
        self.user_info = self.get_user_info()
        self.myid = ''

    def get_user_info(self):

        ensure_dir('user_info/')

        file_list = listdir('user_info/')

        if 'user_info.json' not in file_list:
            with open('user_info/user_info.json', 'w') as f:
                json.dump({}, f)

        with open('user_info/user_info.json', 'r') as f:
            user_info = json.load(f)

        return user_info

    def create_account(self):

        done = False

        while not done:

            id = input('please enter a new id:')

            if id in self.user_info.keys():
                print(f'{id} already exists!')
                sleep(1)
                system('cls')
            else:
                pw = input('please enter password:')
                done = True
                self.save_user_info(id,pw)
                print('account created!!')
                sleep(1)
                system('cls')

    def save_user_info(self,id,pw):
        self.user_info[id] = pw

        with open('user_info/user_info.json','w') as f:
            json.dump(self.user_info,f)

    def login(self):
        id = input('please enter id:')
        pw = input('please enter password:')

        if id in self.user_info.keys() and pw == self.user_info[id]:
            self.myid = id
            return True
        else:
            return False

class post():

    mypath = 'posts/'

    def __init__(self,id):

        self.id = id
        self.posts = self.get_post()

    def get_post(self):
        ensure_dir(self.mypath)

        return listdir(self.mypath)

    def write_post(self):

        while True:

            title = input('title : ')

            if f'{title}.txt' in self.posts:
                print('THERE IS A SAME POST.\nPLEASE CHOOSE ANOTHER TITLE')
                sleep(1)
                system('cls')
            else:
                with open(f"{self.mypath}{title}.txt",'w') as f:
                    done = False
                    f.write(f"title = {title}\ndate : {datetime.today()}\nwritten by {self.id}\n\n\n")
                    print('CONTENTS\n')
                    while not done:
                        try:
                            line = stdin.readline()
                            f.write(line)
                        except KeyboardInterrupt:
                            system('cls')
                            done = True

                    f.write('\nCOMMENTS\n')
                break

    def read_post(self,filename):

        with open(f"{self.mypath}{filename}",'r') as f:
            lines = f.readlines()

            for line in lines:
                print(line)
            
        idx = input('ADD COMMENT? Y/N >>')

        if idx == 'Y' or idx == 'y':
            self.add_post(filename)
            system('cls')
        else:
            system('cls')
    
    def add_post(self,filename):
        
        with open(f"{self.mypath}{filename}",'a') as f:
            done = False
            f.write(f'{self.id} wrote\n')
            while not done:
                try:
                    line = stdin.readline()
                    f.write(line)
                except KeyboardInterrupt:
                    f.write('\n')
                    done = True
        
if __name__ == '__main__':
    main_menu_ui()