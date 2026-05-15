const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.get('/', (req, res) => {
    res.send(`
        <h2>Event Registration Form</h2>
        <form action="/submit" method="POST">
            Name:
            <input type="text" name="name"><br><br>
            Email:
            <input type="email" name="email"><br><br>
            Event Name:
            <input type="text" name="event"><br><br>
            <button type="submit">Register</button>
        </form>
    `);
});
app.post('/submit', (req, res) => {
    const { name, email, event } = req.body;
    res.send(`
        <h2>Registration Successful</h2>
        <p><b>Name:</b> ${name}</p>
        <p><b>Email:</b> ${email}</p>
        <p><b>Event:</b> ${event}</p>
    `);
});
app.listen(3000, () => {
    console.log("Server running on port 3000");
});