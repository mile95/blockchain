from __future__ import annotations

import hashlib


class BlockChain:
    def __init__(self, blocks: [Block]) -> None:
        self.blocks = blocks

    def display(self) -> None:
        print("Hashes:")
        for i, b in enumerate(self.blocks):
            print(f"Block {i}: {b.hash}")
        print("Data:")
        for i, b in enumerate(self.blocks):
            print(f"Block {i}: {b.data}")


class Block:
    def __init__(self, prev_block_hash: str, transactions: [Transaction]) -> None:
        self.prev_block_hash = prev_block_hash
        self.transactions = transactions
        self.data = (
            "-".join([t.to_string() for t in transactions]) + "#" + prev_block_hash
        )
        self.hash = hashlib.sha256(self.data.encode()).hexdigest()


class Transaction:
    def __init__(self, from_client: str, to_client: str, amount: double) -> None:
        self.from_client = from_client
        self.to_client = to_client
        self.amount = amount

    def to_string(self) -> str:
        return f"{self.from_client}.{self.to_client}.{self.amount}"


def main() -> int:
    initial_block = Block(
        "",
        [
            Transaction("A", "B", 10.2),
            Transaction("C", "B", 2.0),
            Transaction("C", "A", 8.4),
        ],
    )
    second_block = Block(
        initial_block.hash,
        [
            Transaction("B", "A", 12.3),
            Transaction("C", "D", 5.1),
            Transaction("A", "B", 3.0),
        ],
    )
    third_block = Block(
        second_block.hash,
        [
            Transaction("A", "B", 9.2),
            Transaction("C", "B", 1.3),
            Transaction("D", "A", 2.2),
            Transaction("F", "C", 8.9),
        ],
    )

    chain = BlockChain([initial_block, second_block, third_block])
    chain.display()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
