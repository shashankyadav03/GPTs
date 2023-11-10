# Create a web API using FastAPI with a route to products.
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Route to /products
# Returns a list of products
@app.get("/products")
def get_products():
    return [{"id": 1, "name": "Product 1"}, {"id": 2, "name": "Product 2"}]

# Route to /products/{id}
# Returns a single product
@app.get("/products/{id}")
def get_product(id: int):
    return {"id": id, "name": "Product " + str(id)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
