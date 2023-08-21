#!/usr/bin/node
const arg = process.argv;
const myId = arg[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + myId;
const request = require('request');

function getRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if(error) {
        reject(error)
        } else {
          resolve(JSON.parse(body).name)
	}
    });
  });
}

request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const myData = JSON.parse(body).characters;
   //myData.forEach((character) => {
	for (const dat of myData) {
	   try {
	   const myResult = await getRequest(dat);
		   console.log(myResult)
	   }
	   catch (error) {
		   console.log(error)
	   }
      };
    }
});
