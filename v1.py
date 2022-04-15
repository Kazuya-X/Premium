import os
try:os.system('mkdir OK')
except:pass
try:os.system('mkdir CP')
except:pass
if __name__ == "__main__":
        try:
                __import__("scrypt").__key__()
        except Exception as e:
                exit(str(e))
