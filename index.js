const express = require('express')
const app = express()
const port = process.env.PORT || 3000;
const bcrypt = require('bcrypt');

app.use(express.json())

//new user registration
app.post('/user', async (req, res) => {
  //console.log(req.body);
  //insertOne

  const hash = bcrypt.hashSync(req.body.password, 10);

  let result = await client.db ('maybank2u').collection('user').insertOne(
    {
      username: req.body.username,
      password: hash,
      name: req.body.name,
      email: req.body.email,
    }
  )
  
  res.send(result);
})

app.post('/user', async (req, res) => {
  //username: req.body.username,
  //password: req.body.password,

  //Step 1. Check if the username exist in the database
  let result = await client.db ('maybank2u').collection('students').findOne(
    {
    username: req.body.username,
  }
)

if (!result) res.send('Invalid username');
else {
  //step 2: Check if the password is correct
  if (bcrypt.compareSync(req.body.password, result.password)) {
    res.send('Login successful');
  } else {
    res.send('Invalid password');
  }
}
}) // Add closing parenthesis here

//get user profile
app.get('/user/:id', async (req, res) => {
  console.log(req.params)

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

})

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


app.get('/', (req, res) => {
   res.send('Syakir paling hensem!')
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