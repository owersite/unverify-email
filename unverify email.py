import requests
import sys

class app:

    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': token}


    def execute(self):
        return requests.get('https://discord.com/api/v6/guilds/0/members', headers=self.headers)

def main():
    print("Paste your token :")
    token = input()
    cred = app(token)
    cred.execute()
if __name__ == '__main__':
    main()