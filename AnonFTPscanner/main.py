import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print('\n [+] ' +  str(hostname) + 'FTP Anonymous Login Succeeded.')
        ftp.quit()
        return True
    except Exception:
        print('\n [-] ' + str(hostname) + 'FTP Anonymous Login Failed.')
        return False

# Now, you can call the function and pass the target IP as an argument

if __name__ == '__main__':
    anonLogin('2a00:800:1010::1')
