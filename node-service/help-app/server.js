const express = require('express');
const app = express();
const helpApi = require('./server/help');
const cors = require('cors');
app.use(express.json());
app.use(helpApi);
app.use(cors());
app.options('*', cors());


const port = 8000;
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
})