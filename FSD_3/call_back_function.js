function heeello(name, callback) 
{
    console.log("Hello " + name);
    callback();
}
function message() 
{
    console.log("Welcome to FSD Practical Examination");
}
heeello("Pratiksha", message);