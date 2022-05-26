import codecs
import os
import sys
import time
import traceback
import win32con
import win32evtlog
import win32evtlogutil
import winerror
import pandas as pd
import csv



def open_file_to_save(the_time,evt_id,msg):
    pass
    # f = open(r'C:\Users\User 1\Desktop\Testing_apui\id.csv', 'w') # открытие для записи
    # f.close()
    # with open(file=r'C:\Users\User 1\Desktop\Testing_apui\id.csv', mode='a', encoding='ANSI') as file:
    #
    #     file.write(f'\n{the_time,evt_id,msg}')

  #### разобраться с записью в столбцы
    # df = pd.read_csv(r'C:\Users\User 1\Desktop\Testing_apui\id.csv')
    # # edit cell based on 0 based index b1=1,0
    # # df[[1,2]] = 1213213213
    # # # write output
    # print(df)
    # df.to_csv(r'C:\Users\User 1\Desktop\Testing_apui\id.csv')


def shutdown_now():
    os.system('shutdown -s')

# ----------------------------------------------------------------------
def getEventLogs(server, logtype):
    hand = win32evtlog.OpenEventLog(server, logtype)
    total = win32evtlog.GetNumberOfEventLogRecords(hand)
    print(
    "Total events in %s = %s" % (logtype, total))
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    try:
        events = 1
        while events:
            events = win32evtlog.ReadEventLog(hand, flags, 0)

            for ev_obj in events:
                the_time = ev_obj.TimeGenerated #.Format()  # '12/23/99 15:54:09'
                evt_id = str(winerror.HRESULT_CODE(ev_obj.EventID))
                msg = win32evtlogutil.SafeFormatMessage(ev_obj, logtype)
                # computer = str(ev_obj.ComputerName)
                # cat = ev_obj.EventCategory
                ##        seconds=date2sec(the_time)
                number_process_coming= {'50103','42'}
                number_pricess_exit = {'7001', '27', '25', '32', '18', '30', '1', '107'}
                if evt_id in number_process_coming:
                    open_file_to_save(str(the_time),evt_id,msg)
                elif    evt_id in number_pricess_exit:   ### написать исклшючение если уже записал время
                    open_file_to_save(str(the_time), evt_id, msg)

    except:
        print(
        traceback.print_exc(sys.exc_info()))
        print(ValueError)

if __name__ == '__main__':
    # open_file_to_save('PyCharm')
    # shutdown_now()
    server = "Localhost" # None = local machine
    logType = "System"
    basePath = r"C:\Users\User 1\Desktop\Testing_apui"
    #path = os.path.join(basePath, "%s_%s_log.log" % (server,  logType ))
    getEventLogs(server, logType)
