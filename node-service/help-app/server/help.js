const express = require('express');
const router = express.Router();

router.get("/help/get-all-help/",  (req, res) =>{
    res.json({ message: 'Resoponse From Node Js App' , data: {
            "name": "test data"
        }});
});

module.exports = router;