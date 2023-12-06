from web3 import Web3

web3 = Web3()
web3.eth.account.enable_unaudited_hdwallet_features()

with open('seed_phrases.txt') as f: seeds = f.read().splitlines()

data = []
for seed in seeds:
    acc = web3.eth.account.from_mnemonic(seed, account_path="m/44'/60'/0'/0/0")
    # data.append(f'{seed}:{acc.key.hex()}:{acc.address}')
    data.append(f'{acc.key.hex()}')

with open(f'private_keys.txt', 'a+') as f:
    f.write('\n'.join([acc for acc in data]))

print(f'converted {len(seeds)} seed phrases')
input('\n > Exit')
