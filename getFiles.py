import os
import shutil

# PATH : str = "C:\Users\Prianshu\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\
# LocalState\Assets"
DESTINATION: str = 'two'


def get_path():
    appdata: str = os.getenv('LOCALAPPDATA')
    print(appdata)
    assets_dir: str = appdata + "\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
    return assets_dir


def copy_files():
    src: str = get_path()
    des: DESTINATION = DESTINATION
    try:
        for file in os.listdir(src):
            shutil.copy2(os.path.join(src, file), des)
    except Exception as error:
        return "Error : "
    return "Success!"


def ren() -> str:
    seq: int
    try:
        for file in os.listdir('two'):
            src = f"two/{file}"
            des = "two/hello.jpeg"
            os.rename(src, des)
        return f"Success..."
    except Exception as e:
        return f"error: {e}"


# print(copy_files())

