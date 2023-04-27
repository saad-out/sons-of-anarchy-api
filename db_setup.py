import os
import sys
from dotenv import load_dotenv

load_dotenv()

db_password = os.getenv('MYSQL_USER_PASSWORD')

if db_password:
    # create a copy setup file with same content
    with open('db_setup.sql', 'r', encoding='UTF-8') as file:
        sql_script = file.read()
    with open('db_setup_copy.sql', 'w', encoding='UTF-8') as file:
        file.write(sql_script)
    
    # replace the password in the copy file
    with open('db_setup_copy.sql', 'w', encoding='UTF-8') as file:
        final_script = file.write(sql_script.replace('${MYSQL_USER_PASSWORD}', db_password))
        print(final_script)
    
    # run the copy file
    os.system('cat db_setup_copy.sql | sudo mysql')
    # remove the copy file
    os.remove('db_setup_copy.sql')
else:
    sys.stderr.write('MYSQL_USER_PASSWORD not found in .env file\n')