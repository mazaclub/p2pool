import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '05fea901'.decode('hex')
P2P_PORT = 11835
ADDRESS_VERSION = 88
RPC_PORT = 11832
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '0x000003ae7f631de18a457fa4fa078e6fa8aff38e258458f8189810de5d62cede')) and
            (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1000*100000000 >> (height + 1)//950000
POW_FUNC = data.hash256
BLOCK_PERIOD = 120 # s
SYMBOL = 'testMAZA'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Mazacoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Mazacoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.mazacoin'), 'mazacoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://mazacha.in/testnet/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://mazacha.in/testnet/address/'
TX_EXPLORER_URL_PREFIX = 'https://mazacha.in/testnet/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
