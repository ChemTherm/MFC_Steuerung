# from TinkerForgeHelperLib.src.TinkerForgeHelperLib import TFH

import json
from tinkerforge_lib import *
from tkinter_lib import *
import time


def main():
    t0 = time.time()

    with open('MFC_test_Settings.json', 'r') as config_file:
        config = json.load(config_file)

    
    ipcon = IPConnection()
    ipcon.connect("localhost", 4223)
    device_list = setup_devices(config, ipcon)
    window, frames = setup_gui(config)

    entry_list = {'File': config['PATH']['SaveFile'],  
                  'MFC': create_set_mfc_entries(window, device_list['MFC'], frames), }
    
    label_list = {'MFC': create_mfc_labels(window, device_list['MFC'], frames, config)}
    
    entry_list['Save']  = setup_frames_labels_buttons(window, frames, config, device_list, entry_list, label_list)
    tk_loop(window, config, device_list, label_list, entry_list) 

    
    window.mainloop()
    print("shutting down...")
    [mfc.stop() for mfc in device_list['MFC']]

    time.sleep(2)
    ipcon.disconnect()
    print("bye bye") 
    
if __name__ == "__main__":
    main()