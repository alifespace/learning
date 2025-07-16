import modal


python_image = (
    modal.Image.from_registry("python:3.12-slim-bookworm")
    .pip_install("requests", "numpy", "pandas", "matplotlib")
)

porth_image = (
    modal.Image.from_registry("pytorch/pytorch:2.7.1-cuda12.8-cudnn9-runtime")
    .pip_install("requests")
)
