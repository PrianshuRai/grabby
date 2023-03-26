import os
import shutil
from datetime import datetime

# PATH : str = "C:\Users\Prianshu\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\
# LocalState\Assets"
DESTINATION: str = ''
SOURCE: str = ''


def get_path():
    assets_dir = ''
    try:
        appdata: str = os.getenv('LOCALAPPDATA')
        if appdata is None:
            raise ValueError
        print(appdata)
        assets_dir: str = os.path.join(appdata, "Packages",
                                       "Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy",
                                       "LocalState", "Assets"
                                       )
    except FileNotFoundError as x:
        print(f"Error: Could not find file path. {x}")
        return
    except Exception as x:
        print(f"Error: an Unexpected error occured {x}")
    return assets_dir


def copy_files():
    src: str = 'D:\onfield\Lessons\one'  # get_path() // TODO: change to get_path
    des: DESTINATION = DESTINATION
    if des[1:3] != ':/':
        return "PathError"
    try:
        for file in os.listdir(src):
            shutil.copy2(os.path.join(src, file), des)
    except Exception as error:
        return f"Error : {error}"
    return "Success!"


def ren(renameTxt="spotlight") -> str:
    seq: int
    date_time = datetime.today()
    date_str = f"{date_time.day}-{date_time.month}-{date_time.year}"
    try:
        for file in os.listdir('two'):
            print(file)
            time_str = f"{date_time.now().time().hour}_" \
                       f"{date_time.now().time().minute}_" \
                       f"{date_time.now().time().second}_" \
                       f"{date_time.now().time().microsecond}"
            src = f"{DESTINATION}/{file}"
            des = f"{DESTINATION}/{renameTxt}_{date_str}_{time_str}.jpg"
            print()
            os.rename(src, des)
        return f"Rename Success!"
    except Exception as e:
        print(f"rename error: {e}")
        return f"Unsuccessful"

# print(copy_files())
