# blockchain

Minimal blockchain implementation in Python.

Learn by doing.

## How to run

No need to install external packages, this script only makes use of pythons standard lib.

`python3 main.py`

The scripts outputs a blockchain.

Example output:

```bash 
$ python3 main.py

Hashes:
Block 0: a1be11c3d461e48f952988bafbba4a155328aaf7a6f86b59cdbf95b78cc79dff
Block 1: 0c6f9fc8669634fc8541175f2e6b49d68e803449b9f4e459f01731e7074d6234
Block 2: 0dd6796f9227ad5f58a4e898f312bc6b3ad75a70d5c1828cd4c48a0f0bf69527
Data:
Block 0: A_B_10.2-C_B_2.0-C_A_8.4#
Block 1: B_A_12.3-C_D_5.1-A_B_3.0#a1be11c3d461e48f952988bafbba4a155328aaf7a6f86b59cdbf95b78cc79dff
Block 2: A_B_9.2-C_B_1.3-D_A_2.2-F_C_8.9#0c6f9fc8669634fc8541175f2e6b49d68e803449b9f4e459f01731e7074d6234

```

The data of a block can be interpreted as:

`<transaction>-<transaction>-<transaction>#<hash_of_previously_block>`

A transaction can be interpreted as:

`<from_client>_<to_client>_<amount>`

So, block 1 contains:

1. Transaction where B transfered `12.3` to A
2. Transaction where C transfered `5.1` to D
3. Transaction where A transfered `3.0` to B
4. Hash of block 0: `a1be11c3d461e48f952988bafbba4a155328aaf7a6f86b59cdbf95b78cc79dff`

