import modal

app = modal.App("python_test")
python_image = (
    modal.Image.from_registry("python:3.12-slim-bookworm")
    .pip_install("requests", "numpy", "pandas", "matplotlib", "duckdb")
)

@app.function(image=python_image)
def matrix_generate(m, n):
    import numpy as np
    return np.random.rand(m, n)

@app.local_entrypoint()
def main():
    A = matrix_generate.remote(100, 20)
    print(A)