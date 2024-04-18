import os

def create_directories(base_path):
    directories = [
        'data/raw',
        'data/processed',
        'data/external',
        'notebooks/exploration',
        'notebooks/experiments',
        'models/checkpoints',
        'models/final',
        'logs/training_logs',
        'logs/evaluation_logs',
        'tests/unit_tests',
        'tests/integration_tests',
        'docs',
        'config'
    ]
    
    for directory in directories:
        path = os.path.join(base_path, directory)
        os.makedirs(path, exist_ok=True)
        print(f"Created directory: {path}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python setup_project.py <project_root_path>")
        sys.exit(1)
    
    project_root = sys.argv[1]
    create_directories(project_root)
    print("Project structure created successfully!")

