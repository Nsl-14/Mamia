from fastapi import FastAPI
from mediaflow_proxy.main import app as mediaflow_app  # Import mediaflow app
import httpx
import re
import string

# Initialize the main FastAPI application
app = FastAPI()

# Manually add only non-static routes from mediaflow_app
for route in mediaflow_app.routes:
    if route.path != "/":  # Exclude the static file path
        app.router.routes.append(route)

# Run the main app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)
