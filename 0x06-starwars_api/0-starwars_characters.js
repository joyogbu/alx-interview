#!/usr/bin/node
const arg = process.argv;
const my_id = arg[2]
const url = "https://swapi-api.alx-tools.com/api/films/" + my_id;
const request = require('request')
request(url, function(error, response, body) {
	if (error)
		console.log(error)
	else {
		const myData = JSON.parse(body).characters;
		myData.forEach((character) => {
			request(character, function (error, response, body) {
        		console.log(JSON.parse(body).name);
			});
		});
	}
});
