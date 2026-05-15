const express = require('express');
const app = express();
app.use(express.json());
let products = [
    {
        id: 1, 
        name: "Laptop", 
        price: 50000 
    }
];
app.get('/products', (req, res) => 
    {
    res.json(products);
});
app.post('/products', (req, res) => 
    {
        const newProduct = {
            id: products.length + 1,
            name: req.body.name,
            price: req.body.price
        };
        products.push(newProduct);
        res.send("Product Added Successfully");
    });
app.listen(3000, () => 
    {
        console.log("Server running on port 3000");
    });
app.delete('/products/:id', (req, res) => {

    const id = parseInt(req.params.id);

    products = products.filter(product => product.id !== id);

    res.send("Product Deleted Successfully");
});