import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f8b503df'.decode('hex')
P2P_PORT = 12835
ADDRESS_VERSION = 50
RPC_PORT = 12832
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '00000c7c73d8ce604178dae13f0fc6ec0be3275614366d44b1b4b5c6e238c60c')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1000*100000000 >> (height + 1)//950000
POW_FUNC = data.hash256
BLOCK_PERIOD = 120 # s
SYMBOL = 'MAZA'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Mazacoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Mazacoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.mazacoin'), 'mazacoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://mazacha.in/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://mazacha.in/address/'
TX_EXPLORER_URL_PREFIX = 'https://mazacha.in/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
