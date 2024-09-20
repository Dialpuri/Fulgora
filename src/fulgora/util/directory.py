from pathlib import Path
from datetime import datetime


def create(args) -> Path: 
    output_dir = Path(args.outdir)
    output_dir.mkdir(exist_ok=True, parents=True)
    time = datetime.now()

    formatted_model = Path(args.model).stem
    run_dir = output_dir / f"{formatted_model}_{time.strftime('%d_%m_%Y-%H:%M:%S')}"

    run_dir.mkdir(exist_ok=True)
    return run_dir