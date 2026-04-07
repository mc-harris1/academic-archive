#!/usr/bin/env python3

"""match.py: Exact pattern matching using the Z-algorithm on FASTA files."""

import sys
from pathlib import Path

import numpy as np


def get_resource_resolver():
    current_file = Path(__file__).resolve()

    for parent in (current_file.parent, *current_file.parents):
        if (parent / "pyproject.toml").exists():
            graduate_school_dir = parent / "graduate-school"

            if str(graduate_school_dir) not in sys.path:
                sys.path.insert(0, str(graduate_school_dir))

            from utilities.path_utils import resolve_local_resource_path

            return resolve_local_resource_path

    raise RuntimeError(f"Could not locate repository root above {current_file}.")


resolve_local_resource_path = get_resource_resolver()


class PatternMatching:
    def __init__(self, text, pattern):
        self.text = text  # text to be searched
        self.pattern = pattern  # pattern to search the text for
        self.full_s = (
            self.pattern + "$" + self.text
        )  # string concatenating the pattern and text strings
        self.str_len = len(self.full_s)  # get length of concatenated string
        self.Z = np.zeros(self.str_len)  # create Z array initialized with 0's
        self.compute_z()  # call z algorithm method to compute Z array

    def compute_z(self):
        # initialize left and right indices of Z array to 0
        left_z_box_index = 0
        right_z_box_index = 0

        # loop through concatenated string
        for i in range(1, self.str_len):
            if i > right_z_box_index:  # Compute new interval
                left_z_box_index = i
                right_z_box_index = i
                self.explicit_check(i, right_z_box_index, left_z_box_index)  # explictly check
            else:
                j = i - left_z_box_index  # Same interval; j prefix matches remain in the Z box.

                if self.Z[j] < right_z_box_index - i + 1:
                    self.Z[i] = self.Z[j]
                else:
                    # Compute new interval
                    left_z_box_index = i
                    self.explicit_check(i, right_z_box_index, left_z_box_index)  # explictly check

        self.search()

    def explicit_check(self, index, r_ind, l_ind):
        while (
            r_ind < self.str_len and self.full_s[r_ind - l_ind] == self.full_s[r_ind]
        ):  # Compute new interval
            r_ind += 1  # grow Z box by one to the right

        self.Z[index] = r_ind - l_ind
        r_ind -= 1  # shrink Z box by one to the left

    def search(self):
        for i in range(self.str_len):
            if self.Z[i] == len(self.pattern):
                print(
                    "Found pattern in text, beginning at following index: "
                    + str(i - len(self.pattern) - 1)
                )


if __name__ == "__main__":
    pattern = sys.argv[1]  # take in first argument as pattern
    text = sys.argv[2]  # take in second argument as text

    text_path = resolve_local_resource_path(__file__, text)

    with open(text_path) as f:  # open FASTA file
        content = f.readlines()  # read lines of FASTA file into list
        content = content[1:]  # ignore first line
        text = "".join(content).rstrip("\n").upper()  # strip newlines and convert to upper-case

    run = PatternMatching(text, pattern)  # create instance of PatternMatching class
