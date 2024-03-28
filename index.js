const express = require('express')
const app = express()
const port = process.env.PORT || 3000;

app.use(express.json())

app.get('/', (req, res) => {
   res.send('Hello LOVEEE!')
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
    //await client.connect();
    // Send a ping to confirm a successful connection
    //await client.db("admin").command({ ping: 1 });
    //console.log("Pinged your deployment. You successfully connected to MongoDB!");

    // insert a document into the database
    //let result = await client.db ('maybank2u').collection('students').insertOne({
      //name: 'Ridhuwan' ,
      //age : 25,
      //status: 'A',
      //faculty: 'FTKEK'
    //});

      let result = await client.db ('maybank2u').collection('students').findOne(
        {
          name: 'Ahmad'
        }
        //{ _id: new ObjectId("660511dd96a7f358b46eca40") },
        //{ $set: { name: 'Ahmad' } }
      ).toArray()        
    console.log(result)


    //console.log("You successfully connected to MongoDB!GOOD JOB BRO!" + result.insertedId)

    //let result = await client.db ('maybank2u').collection('students').find().toArray();
    //console.log(result);

  } finally {
    // Ensures that the client will close when you finish/error
    //await client.close();
  }
}
run().catch(console.dir);


