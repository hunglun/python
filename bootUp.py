import time
import ratools.lnx.logixtools as logixTools
import ratools.cip.channel as channel
primaryChan = channel.create('primary')
def start_timer():
    start_time = time.time()
    print "start to boot"
    logixTools.waitForResetEnd(timeout=100)
    print("--- %s seconds ---" % (time.time() - start_time))
def reboot():
    start_time = time.time()
    print "start to boot"

    logixTools.resetController(timeout=100,forward=True,ramBad=True)
    print("--- %s seconds ---" % (time.time() - start_time))


def reset(ramBad=False):
    partnerChan.closeConnection()
    print "resetController"
    start_time = time.time()
    logixTools.resetController(forward=True,ramBad=ramBad)
    partnerChan.select()
    logixTools.waitForResetEnd(timeout=100)
    print("--- %s seconds ---" % (time.time() - start_time))
    partnerChan.openConnection()
    logixTools.dbgUnlockObject(partnerChan) # For cGLX partner
    primaryChan.select()
