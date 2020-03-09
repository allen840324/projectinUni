import math
import wave
import numpy as np
import pylab as pl
import Volume as vp

# method 1: absSum
def calVolume(waveData, frameSize, overLap):
    wlen = len(waveData)
    step = frameSize - overLap
    frameNum = int(math.ceil(wlen*1.0/step))
    volume = np.zeros((frameNum,1))
    for i in range(frameNum):
        curFrame = waveData[np.arange(i*step,min(i*step+frameSize,wlen))]
        curFrame = curFrame - np.median(curFrame) # zero-justified
        volume[i] = np.sum(np.abs(curFrame))
    return volume

# method 2: 10 times log10 of square sum
def calVolumeDB(waveData, frameSize, overLap):
    wlen = len(waveData)
    step = frameSize - overLap
    frameNum = int(math.ceil(wlen*1.0/step))
    volume = np.zeros((frameNum,1))
    for i in range(frameNum):
        curFrame = waveData[np.arange(i*step,min(i*step+frameSize,wlen))]
        curFrame = curFrame - np.mean(curFrame) # zero-justified
        volume[i] = 10*np.log10(np.sum(curFrame*curFrame))
    return volume
# ============ test the algorithm =============
# read wave file and get parameters.
fw = wave.open('output.wav','r')
params = fw.getparams()
print(params)
nchannels, sampwidth, framerate, nframes = params[:4]
strData = fw.readframes(nframes)
waveData = np.fromstring(strData, dtype=np.int16)
waveData = waveData*1.0/max(abs(waveData))  # normalization
fw.close()

# calculate volume
frameSize = 256
overLap = 128
volume11 = vp.calVolume(waveData,frameSize,overLap)
volume12 = vp.calVolumeDB(waveData,frameSize,overLap)

# plot the wave
time = np.arange(0, nframes)*(1.0/framerate)
time2 = np.arange(0, len(volume11))*(frameSize-overLap)*1.0/framerate
pl.subplot(311)
pl.plot(time, waveData)
pl.ylabel("Amplitude")
pl.subplot(312)
pl.plot(time2, volume11)
pl.ylabel("absSum")
pl.subplot(313)
pl.plot(time2, volume12, c="g")
pl.ylabel("Decibel(dB)")
pl.xlabel("time (seconds)")
pl.show()