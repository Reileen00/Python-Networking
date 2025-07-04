import ftplib import FTP

host="videoftptut.bplaced.net"
user="videoftptut"
password="neural123"

with FTP(host) as ftp:
  ftp.login(user=user,passwd=password)
  print(ftp.getwelcome())

  with open('myupload.txt','rb') as f:
    ftp.storebinary("STOR "+"upload.txt", f)
    
  ftp.cwd("mydir")
  
  with open('myspecialfile.txt','wb') as f:
    ftp.retrbinary('RETR'+'otherfile.txt',f.write,1024)
  ftp.quit():password
