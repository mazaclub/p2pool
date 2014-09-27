from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['mazacoin']
SHARE_PERIOD = 30 # seconds between pool shares
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 7 # shares
SPREAD = 25 # blocks
IDENTIFIER = 'b497d1a69c84e7e1'.decode('hex')
PREFIX = '73b291a3e8c084d2'.decode('hex')
P2P_PORT = 14476
MIN_TARGET = 0
MAX_TARGET = 2**256//2**40 - 1
PERSIST = False
WORKER_PORT = 14477
BOOTSTRAP_ADDRS = 'p2pool.maza.club p2pool-2.maza.club'.split(' ')
ANNOUNCE_CHANNEL = '#mazacoin-p2pool'
VERSION_CHECK= lambda v: True
