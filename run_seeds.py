from seeds import seed_inheritance, seed_polymorphism, seed_relationship_types, seed_validation, seed_encapsulation, seed_abstraction
import subprocess

def run_seeds_and_script(module_name):
    # Dynamically call the seed function based on the module name if it exists
    seed_function = globals().get(f'seed_{module_name}')
    if seed_function:
        seed_function()
        print(f"Seed function for {module_name} executed.")
    subprocess.run(['python', f'{module_name}.py'])
    print(f"{module_name}.py executed.")