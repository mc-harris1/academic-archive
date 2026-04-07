#!/usr/bin/env python3

"""center_star.py: approximate the optimal multiple alignment of a
set of sequences using center star method."""

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


class CenterStar:
    def __init__(self, sequences, alpha, beta):
        self.sequences = sequences
        self.size = len(self.sequences)
        self.alpha = alpha
        self.beta = beta
        self.center_star = None
        self.mult_aligns = []
        self.S = np.zeros((self.size, self.size), dtype=int)

    def generate_score_matrix(self):
        for i in range(self.size):
            for j in range(self.size):
                self.S[i, j] = self.compute_distance(self.sequences[i], self.sequences[j], 0)

    def compute_distance(self, seq_a, seq_b, opt):
        n = len(seq_a) + 1
        m = len(seq_b) + 1

        F = np.zeros((n, m), dtype=int)

        F[0, :] = np.arange(0, self.alpha * m, self.alpha)
        F[:, 0] = np.arange(0, self.alpha * n, self.alpha)

        for i in range(1, n):
            for j in range(1, m):
                Match = F[i - 1, j - 1] + self.get_cost(seq_a[i - 1], seq_b[j - 1])
                Delete = F[i - 1, j] + self.beta
                Insert = F[i, j - 1] + self.beta
                F[i, j] = min(Match, Insert, Delete)

        if opt == 0:
            return F[n - 1, m - 1]  # return pairwise alignment distance
        else:
            return F  # return full distance matrix

    def get_cost(self, seq_a_idx, seq_b_idx):
        if seq_a_idx == seq_b_idx:
            return 0
        else:
            return self.alpha

    def get_center_sequence(self):
        dist_pair_scores = np.triu(self.S)
        rows = dist_pair_scores.sum(axis=1)
        cols = dist_pair_scores.sum(axis=0)
        total = np.add(rows, cols)

        self.center_star = self.sequences[total.argmin()]
        return self.center_star

    def align_sequences(self, F, seq_center, seq_i):
        Align_seq_center = ""
        Align_seq_i = ""
        i = len(seq_center)
        j = len(seq_i)

        while i > 0 or j > 0:
            if (
                i > 0
                and j > 0
                and F[i, j] == F[i - 1, j - 1] + self.get_cost(seq_center[i - 1], seq_i[j - 1])
            ):
                Align_seq_center = seq_center[i - 1] + Align_seq_center
                Align_seq_i = seq_i[j - 1] + Align_seq_i
                i -= 1
                j -= 1
            elif i > 0 and F[i, j] == F[i - 1, j] + self.beta:
                Align_seq_center = seq_center[i - 1] + Align_seq_center
                Align_seq_i = "-" + Align_seq_i
                i -= 1
            else:
                Align_seq_center = "-" + Align_seq_center
                Align_seq_i = seq_i[j - 1] + Align_seq_i
                j -= 1
        return Align_seq_center, Align_seq_i

    def get_mult_alignment(self):
        for i in range(self.size):
            if self.sequences[i] != self.center_star:
                mat = self.compute_distance(self.center_star, self.sequences[i], 1)
                self.mult_aligns.append(
                    self.align_sequences(mat, self.center_star, self.sequences[i])
                )

        for i in range(len(self.mult_aligns)):
            if self.center_star is not None and len(self.mult_aligns[i][0]) > len(self.center_star):
                self.center_star = self.mult_aligns[i][0]

        for i in range(len(self.mult_aligns)):
            if self.sequences[i] != self.center_star:
                mat = self.compute_distance(self.center_star, self.mult_aligns[i][1], 1)
                self.mult_aligns.append(
                    self.align_sequences(mat, self.center_star, self.mult_aligns[i][1])
                )

        self.mult_aligns = self.mult_aligns[self.size - 1 :]
        print("The multiple sequence alignment is:")
        print(self.center_star)
        for i in range(len(self.mult_aligns)):
            print(self.mult_aligns[i][1], sep="\n")


if __name__ == "__main__":
    fasta_f = sys.argv[1]  # fasta file to be processed
    a = sys.argv[2]  # alpha parameter for cost function
    b = sys.argv[3]  # beta parameter for cost function

    fasta_path = resolve_local_resource_path(__file__, fasta_f)

    with open(fasta_path) as f:
        sequences_l = []
        for ln in f:
            if not ln.startswith(">"):
                sequences_l.append(ln.rstrip())

    run = CenterStar(sequences_l, int(a), int(b))  # create instance of CenterStar

    run.generate_score_matrix()  # compute optimal alignments

    print(f"The center sequence is {run.get_center_sequence()}.")  # find and return center sequence

    run.get_mult_alignment()  # compute and return alignment
