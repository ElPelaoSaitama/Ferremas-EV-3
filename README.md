# Proyecto Ferremas

## Configuración del Entorno Virtual (venv)

1. **Instalar `virtualenv`**:
    ```sh
    pip install virtualenv
    ```

2. **Crear y activar el entorno virtual**:
    ```sh
    virtualenv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS y Linux
    ```

3. **Instalar dependencias**:
    ```sh
    pip install -r requirements.txt
    ```
## Pruebas con Pytest

Para realizar las pruebas, usa:
```sh
pytest -v
```
