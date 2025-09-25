## Project Overview

This repository contains bioinformatics tools for molecular cloning workflows involved in uASPIre cloning. The codebase is currently organized into two main functional modules:

### Core Modules

1. **pASPIre_adaptor_ligation/** - Molecular cloning workflow tools
   - Handles restriction enzyme digestion of plasmid sequences
   - Performs adaptor ligation with sequence-specific left/right adaptors
   - CSV-based batch processing pipeline

2. **primer_annealing_temp/** - PCR primer analysis tools
   - CLI tool for DNA primer sequence analysis
   - Calculates melting temperature (Tm) and annealing times
   - Optimized for Primestar MAX polymerase protocols

## Installation and Setup
Clone the repository

``` bash
    git clone git@github.com:constructivebio/uaspire-cloning-tools.git
```

In the cloned repo directory, create a virtual environment
``` bash    
    python3 -m venv venv
    source venv/bin/activate
```

Install the package in development mode, and dependencies

``` bash
    pip install -e .
    pip install -r requirements.txt
```

## Key Commands

### CLI Tools
```bash
# Primer analysis CLI (installed as 'ci' command)
ci ATCGATCGATCG  # Analyze single primer sequence
ci PRIMER1 PRIMER2  # Analyze multiple sequences

# Run individual modules directly
python -m pASPIre_adaptor_ligation.restriction_digest
python -m pASPIre_adaptor_ligation.adaptor_ligation
python -m primer_annealing_temp.cli
```

## Architecture Overview

### Molecular Cloning Pipeline (pASPIre_adaptor_ligation/)

The cloning workflow follows this sequence:
1. **CSV Parsing** (`parse_csv.py`) - Reads input CSV with sequence data and adaptor specifications
2. **Restriction Digestion** (`restriction_digest.py`) - Uses BioPython to simulate NcoI + SacI double digest, extracting target fragments (filters out 144bp backbone fragments)
3. **Adaptor Ligation** (`adaptor_ligation.py`) - Ligates predefined adaptors from `adaptors.py` to create final constructs
4. **CSV Export** - Optional export of digest products and final ligated sequences

### Data Flow
- Input: CSV files with columns [Sequence, Left_Adaptor, Right_Adaptor]
- Processing: Restriction enzyme analysis using BioPython's restriction module
- Output: Ligated sequences with specified adaptors, optional CSV export

### Adaptor System
- 6 predefined left adaptors (L1-L6) and right adaptors (R1-R6) in `adaptors.py`
- Designed for Illumina sequencing compatibility with specific barcode sequences

### Primer Analysis System (primer_annealing_temp/)
- Uses simplified Tm calculation: `(2 * (A + T)) + (4 * (C + G)) - 5`
- Annealing time logic: 5 seconds for primers >25bp or Tm≥55°C, otherwise 15 seconds
- Structured as installable CLI tool via setuptools entry points

## Dependencies

- **BioPython**: Core dependency for restriction enzyme analysis and sequence manipulation
- **Click**: CLI framework for command-line interfaces
- **CSV**: Built-in Python module for data parsing and export

## Testing

The codebase includes test CSV files (`test_csv.csv`) referenced in main execution blocks. Run individual modules directly to test functionality.