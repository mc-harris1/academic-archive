#!/usr/bin/env python3

"""align.py: Global alignment for sequences using the Needleman Wunsch algorithm on FASTA fles."""

import sys
from pathlib import Path

import numpy as np


def get_resource_resolver():
    current_file = Path(__file__).resolve()

    for parent in (current_file.parent, *current_file.parents):
        if (parent / "pyproject.toml").exists():
            if str(parent) not in sys.path:
                sys.path.insert(0, str(parent))

            from shared.path_utils import resolve_local_resource_path

            return resolve_local_resource_path

    raise RuntimeError(f"Could not locate repository root above {current_file}.")


resolve_local_resource_path = get_resource_resolver()


class GlobalAlignment:
    def __init__(self, sequences, match, mismatch, insert):
        self.sequences = sequences
        self.size = len(self.sequences)
        self.match = match
        self.mismatch = mismatch
        self.insert = insert
        self.aligns = []
        self.F = None

    def compute_scores(self):
        seq_a = self.sequences[0]
        seq_b = self.sequences[1]
        n = len(seq_a) + 1
        m = len(seq_b) + 1

        self.F = np.zeros((n, m), dtype=int)

        self.F[0, :] = np.arange(0, self.match * m, self.match)
        self.F[:, 0] = np.arange(0, self.match * n, self.match)

        for i in range(1, n):
            for j in range(1, m):
                Match = self.F[i - 1, j - 1] + self.get_score(seq_a[i - 1], seq_b[j - 1])
                Delete = self.F[i - 1, j] + self.insert
                Insert = self.F[i, j - 1] + self.insert
                self.F[i, j] = max(Match, Insert, Delete)

        return self.F[n - 1, m - 1]  # return pairwise alignment score

    def get_score(self, seq_a_idx, seq_b_idx):
        if seq_a_idx == seq_b_idx:
            return self.match

        return self.mismatch

    def align_sequences(self):
        seq_a = self.sequences[0]
        seq_b = self.sequences[1]
        Align_seq_a = ""
        Align_seq_b = ""
        i = len(seq_a)
        j = len(seq_b)

        while i > 0 or j > 0:
            if (
                i > 0
                and j > 0
                and self.F is not None
                and self.F[i, j]
                == self.F[i - 1, j - 1] + self.get_score(seq_a[i - 1], seq_b[j - 1])
            ):
                Align_seq_a = seq_a[i - 1] + Align_seq_a
                Align_seq_b = seq_b[j - 1] + Align_seq_b
                i -= 1
                j -= 1
            elif i > 0 and self.F is not None and self.F[i, j] == self.F[i - 1, j] + self.mismatch:
                Align_seq_a = seq_a[i - 1] + Align_seq_a
                Align_seq_b = "-" + Align_seq_b
                i -= 1
            else:
                Align_seq_a = "-" + Align_seq_a
                Align_seq_b = seq_b[j - 1] + Align_seq_b
                j -= 1

        self.aligns.append(Align_seq_a)
        self.aligns.append(Align_seq_b)

    def get_alignment(self):
        for i in range(len(self.aligns)):
            print(self.aligns[i])


if __name__ == "__main__":
    fasta_f = sys.argv[1]  # fasta file to be processed
    x = sys.argv[2]  # match parameter for scoring function
    y = sys.argv[3]  # mismatch parameter for scoring function
    z = sys.argv[4]  # insertion parameter for scoring function

    fasta_path = resolve_local_resource_path(__file__, fasta_f)

    with open(fasta_path) as f:
        sequences_l = []
        for ln in f:
            if not ln.startswith(">"):
                sequences_l.append(ln.rstrip())

    run = GlobalAlignment(
        sequences_l, int(x), int(y), int(z)
    )  # create instance of GlobalAlignment class

    run.compute_scores()  # compute optimal alignments for the pair of sequences

    run.align_sequences()  # align sequences based on scores

    run.get_alignment()  # return the sequence alignment
