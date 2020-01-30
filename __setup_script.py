import os

if __name__=='__main__':
    try:
        os.system('python3  -m venv ~/test_venv')
        os.system('source ~/test_venv/bin/activate')
        os.system('pip install  django==1.11, m3-objectpack==2.2.25 --extra-index-url http://pypi.bars-open.ru/simple/')
        os.system('cd ~/test_venv')
        os.system('django-admin startproject m3_project')
        os.system('python3 m3_project/manage.py runserver 0.0.0.0:8000')
    except:
        print('Bash script error...')
    