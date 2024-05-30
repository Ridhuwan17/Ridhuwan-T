const express = require('express')
const app = express()
const port = process.env.PORT || 3000;
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

app.use(express.json())

//new user registration
app.post('/user', async (req, res) => {
  //console.log(req.body);
  //insertOne

  const hash = bcrypt.hashSync(req.body.password, 10);

  let result = await client.db('maybank2u').collection('user').insertOne(
    {
      username: req.body.username,
      password: hash,
      name: req.body.name,
      email: req.body.email,
    }
  )
  
  res.send(result);
})

app.post('/login', async (req, res) => {
  //username: req.body.username,
  //password: req.body.password,

  //Step 1. Check if the username exist in the database
  let result = await client.db('maybank2u').collection('user').findOne(
    {
    username: req.body.username
  }
);
console.log(result);

if (!result){
  res.send('Invalid username');
}  else {
  //step 2: Check if the password is correct
  if (bcrypt.compareSync(req.body.password, result.password)) {
    //password is correct
    var token = jwt.sign({
      
      _id: result._id,
      username: result.username,
      password: result.password


    }, 'mysupersecretkey', {expiresIn: 10*60 });
    res.send(token);
  } else {
    //password is incorrect
    res.status(401).send ('Invalid password');
  }
}
}) // Add closing parenthesis here

//get user profile

app.get('/user/:id', async (req, res) => {
  
  if (decoded) 
  if (decoded._id != req.params.id) {
    let result = await client.db ('maybank2u').collection('students').findOne(
      {
        _id: new ObjectId (req.params.id),
      })
    //findOne 
    // let result = await client.db ('maybank2u').collection('user').findOne({
    // username: req.params.namadia,
    // password: req.params.emaildia,
    // });
    res.send(result);
  }else {
    res.status(401).send('Unauthorized')
  }
}); // Add closing parenthesis here

//update user account
app.patch('/user/:id', async (req, res) => {
  //updateOne
  //console.log('User profile updated')
  let result = await client.db ('maybank2u').collection('students').updateOne(
    {
      _id: new ObjectId (req.params.id),
    },
    {
      $set: {
        name: req.body.name,
      }
    }
  );
  res.send(result);
})

//delete user account
app.delete('/user/:id', async (req, res) => {
  //deleteOne
  //console.log('User profile deleted')
  let result = await client.db ('maybank2u').collection('students').deleteOne(
    {
      _id: new ObjectId (req.params.id),
    }
  )
  res.send(result)

})

app.delete('/user', async (req, res) => {
})

app.post('/buy', async (req, res) => {
  const token = req.headers.authorization.split(" ")[1];
  console.log(`token: ${token}`);

  var decoded = jwt.verify(token, 'mysupersecretkey');
  console.log(decoded);
  res.send(decoded);
})


app.get('/', (req, res) => {
   res.send('RIDH WAS HERE!')
})

app.listen(port, () => {
   console.log(`Example app listening on port ${port}`)
})

//Path: package.json
const { MongoClient, ServerApiVersion, ObjectId } = require('mongodb');
const uri = "mongodb+srv://B022210140:ridhuwan17@ridhuwan17.y6ssjvq.mongodb.net/?retryWrites=true&w=majority&appName=Ridhuwan17";

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

function verifyToken(req,res,next) {
  const authHeader = req.headers.authorization;
  const token = authHeader.split(' ')[1];

  if (token == null) return res.sendStatus(401);

  jwt.verify(token, 'mysupersecretkey', (err, decoded) => {
    console.log(err)

    if (err) return res.sendStatus(403);

    req.decoded = decoded;

    next();
  });
}

async function run() {
  try {
    // Connect the client to the server	(optional starting in v4.7)
    await client.connect();
    // Send a ping to confirm a successful connection
    await client.db("admin").command({ ping: 1 });
    console.log("Pinged your deployment. You successfully connected to MongoDB!");

    // insert a document into the database
    //let result = await client.db ('maybank2u').collection('students').insertOne({
      //name: 'Ridhuwan' ,
      //age : 25,
      //status: 'A',
      //faculty: 'FTKEK'
    //});

      //let result = await client.db ('maybank2u').collection('students').findOne(
        //{
         // name: 'Ahmad'
        //}
        //{ _id: new ObjectId("660511dd96a7f358b46eca40") },
        //{ $set: { name: 'Ahmad' } }
      //).toArray()        
    //console.log(result)


    //console.log("You successfully connected to MongoDB!GOOD JOB BRO!" + result.insertedId)

    //let result = await client.db ('maybank2u').collection('students').find().toArray();
    //console.log(result);

  } finally {
    // Ensures that the client will close when you finish/error
    //await client.close();
  }
}
run().catch(console.dir); 

