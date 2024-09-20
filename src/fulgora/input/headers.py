import multiprocessing

# %NProcShared=64
# %mem=200GB
# %Chk=job2.chk

def trailing_newline(func): 
    def wrapper(*args, **kwargs):
        return f"{func(*args, **kwargs)}\n"
    return wrapper

def leading_newline(func): 
    def wrapper(*args, **kwargs):
        return f"\n{func(*args, **kwargs)}"
    return wrapper

@trailing_newline
def get_nproc_shared(cpu_count: int) -> str:
    cpu_count = cpu_count if cpu_count else multiprocessing.cpu_count()
    return f"%NProcShared={cpu_count}"

@trailing_newline
def get_memory(memory: str | float) -> str: 
    if isinstance(memory, float): 
        return f"%mem={memory}GB"
    if isinstance(memory, str): 
        memory = memory.lower()
        if memory.rfind("gb") == len(memory)-2:
            return f"%mem={memory.rstrip('gb')}GB"

    raise RuntimeError("Could not create memory header")

@trailing_newline
def get_checkpoint():
    return "%Chk=job.chk"

def create(args):
    header_string = ""
    
    header_string += get_nproc_shared(args.cpus)
    header_string += get_memory(args.memory)
    header_string += get_checkpoint()
    return header_string