import hashlib


def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()


class Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash


class BlockChain:
    def __init__(self):
        lasthash = hashGenerator('12')
        blockhash = hashGenerator("GenesisBlock")

        genesis = Block('gendata', lasthash, blockhash)

        self.chain = [genesis]

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(prev_hash+data)
        block = Block(data, hash, prev_hash)
        self.chain.append(block)


bc = BlockChain()

bc.add_block('1')
bc.add_block('2')
bc.add_block('3')
bc.add_block('4')


for block in bc.chain:
    print(block.__dict__)
