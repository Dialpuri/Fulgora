import argparse
from fulgora.input import convert
from fulgora.input import headers
from fulgora.util import directory


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-model", help="Path to CIF file", required=True)
    parser.add_argument("-cpus", help="CPU cores", default=None, required=False)
    parser.add_argument("-memory", help="Memory (Gb)", default=16, required=False)
    parser.add_argument("-outdir", help="Output Directory", default=16, required=False)

    return parser.parse_args()

def main():
    args = parse_arguments()
    
    base_directory = directory.create(args)
    header_string = headers.create(args)
    gjf_atoms = convert.cif_to_gjf_atoms(args.model)

    