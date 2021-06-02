
import dropbox
import os

local_path = 'C:\Users\HP\Documents\Whitehatjr\Python Vivek\folderA'

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
        
    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, file in os.walk(file_from):
            relative_path = os.path.realpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overWrite'))

def main():
    accessToken = ''
    transferData = TransferData(accessToken)
    fileFrom = input("enter the file path to be transfered from your local system: -")
    fileTo = input("enter your dropbox cloud storage path: -")
    transferData.upload_files(fileFrom, fileTo)
    print("the file has been transfered")

main()