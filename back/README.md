# Backend API

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Setup

1.  Create a virtual environment:
    ```bash
    python -m venv .venv
    ```

2.  Activate the virtual environment:
    - **Windows**:
      ```powershell
      .venv\Scripts\activate
      ```
    - **Mac/Linux**:
      ```bash
      source .venv/bin/activate
      ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Server

Start the development server with:

```bash
fastapi dev main.py
```

The API will be available at http://127.0.0.1:8000.
