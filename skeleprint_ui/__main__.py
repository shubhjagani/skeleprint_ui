if __name__ == '__main__':
    import tpg_gui
    import os

    from shutil import copy2
    
    path = os.path.dirname(tpg_gui.__file__)
    src = path+"/SkelePrint_UI.pyc"

    dst = os.path.join(os.path.expanduser("~"), "Desktop")
    print dst
    copy2(src, dst)

    tpg_gui.vp_start_gui()
