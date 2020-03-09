import _thread
import pyaudio
import time
import os
from math import log10
from statistics import mean


class DbMeter(object):
    def __init__(self, rate=44100, channels=1, frames_per_buffer=4000, chunk=512, format=pyaudio.paInt16,
                 call_back=None):
        super().__init__()
        self.rate = rate
        self.channels = channels
        self.format = format
        self.frames_per_buffer = frames_per_buffer
        self.chunk = chunk
        self.stream = None
        self.started = False
        self.call_back = call_back

    def start(self):
        if self.started:
            return
        self.started = True  
        self.stream = pyaudio.PyAudio().open(format=self.format, channels=self.channels,
                                             rate=self.rate, input=True, output=False, frames_per_buffer=self.chunk)
                                       
        _thread.start_new_thread(self.__calculate, ())

    def __calculate(self):
        while self.started:
            data = self.stream.read(self.chunk, exception_on_overflow=False)
            int_datas = []
            for i in range(0, len(data), 32):
                tar = int.from_bytes(data[i: i + 4], byteorder='little')
                if tar > 0x7FFFFFFF:
                    tar -= 0x100000000
                int_datas.append(tar)

            dbfs_list = [abs(x) & 0xFFFF0000 for x in int_datas]
            mean_val = mean(dbfs_list)

            if mean_val > 0:
                ret_db = 120 + 20 * log10(mean_val / 0x7FFFFFFF)
                if self.call_back is not None:
                    self.call_back(ret_db)

    def stop(self):
        self.started = False
        if self.stream is not None:
            self.stream.close()
            self.stream = None


def call_back_one(db_value):
    #print('call_back_one : %s' % db_value)


def call_back_two(db_value):
    print('call_back_two : %s' % db_value)


#db_meter = DbMeter(call_back=call_back_one)
#db_meter.start()
#time.sleep(600)
#db_meter.call_back = call_back_two
#time.sleep(600)
#db_meter.stop()
