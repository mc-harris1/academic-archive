# CSCI-551-Advanced-Computational-Biology

Examines a variety of algorithmic computational biology topics with an emphasis on elucidating new research problems.

## Workflow

This course currently uses a script-first Python workflow.

- Run homework directly as `.py` files.
- Use the repository root Python environment defined in `pyproject.toml`.
- Keep assignment inputs in `hw/data/` and use matching prefixes, for example `1_match.py` with `1_test.fasta`, `2_align.py` with `2_test.fasta`, and `4_center_star.py` with the `4_*.fasta` files.
- For scripts that consume FASTA data, pass the filename only. The shared path utility in `shared/path_utils.py` resolves it from the local `hw/data/` directory.

This course is not notebook-first today. If a notebook is added later, it should wrap the existing script logic rather than replace it.

## Homework Scripts

### Assignment 1

`hw/1_match.py` performs exact pattern matching.

Parameters:

- `pattern`: query string to search for
- `text_fasta`: FASTA filename from `hw/data/`, such as `1_test.fasta`

Example:

```bash
python graduate-school/courses/csci_551_adv_comp_bio/hw/1_match.py ACTGA 1_test.fasta
```

### Assignment 2

`hw/2_align.py` performs global alignment for two sequences.

Parameters:

- `fasta_file`: FASTA filename from `hw/data/`, such as `2_test.fasta`
- `match`: match score
- `mismatch`: mismatch score
- `insert`: insertion or gap score

Example:

```bash
python graduate-school/courses/csci_551_adv_comp_bio/hw/2_align.py 2_test.fasta 2 -1 -1
```

### Assignment 4

`hw/4_center_star.py` computes a center-star multiple alignment.

Parameters:

- `fasta_file`: FASTA filename from `hw/data/`, such as `4_test.fasta`, `4_test1.fasta`, or `4_test2.fasta`
- `alpha`: mismatch cost parameter
- `beta`: insertion or deletion cost parameter

Example:

```bash
python graduate-school/courses/csci_551_adv_comp_bio/hw/4_center_star.py 4_test2.fasta 1 2
```

### Assignment 5

`hw/5_rmq.py` benchmarks range minimum query performance.

Parameters:

- none

Example:

```bash
python graduate-school/courses/csci_551_adv_comp_bio/hw/5_rmq.py
```
