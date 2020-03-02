const express = require('express');


const app = express();

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*"); // update to match the domain you will make the request from
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.use(express.json()); 
const port = 5000;



app.get('/', (req, res)=>{
	res.json({
		"Name":"Un-Link-1337",
		"status":"Active"
	})
});

app.post('/ch1', (req, res)=>{
	var sol_flag = 'one';
	// console.log(req.body)
	let i_flag = req.body.flag;
	console.log('comming' + i_flag)
	if (sol_flag === i_flag){
		res.json({status:"Success"});
	}
	else{
		res.json({status:'Failed'})
	}
});

// app.post('/ch2', (req, res)=>{
// 	let flag = 'mzctf{1234}'
// 	let i_flag = req.body.flag;
// 	console.log(i_flag)
// 	if (flag === i_flag){
// 		res.json({status:"Success"})
// 	}
// 	else{
// 		res.json({status:'fail'})
// 	}
// });

// app.post('/ch3', (req, res)=>{
// 	let flag = 'mzctf{1234}'
// 	let i_flag = req.body.flag;
// 	console.log(i_flag)
// 	if (flag === i_flag){
// 		res.json({status:"Success"})
// 	}
// 	else{
// 		res.json({status:'fail'})
// 	}
// });


// console.clear()
app.listen(port,()=>{
	console.log(`App listening on ${port}`)
})