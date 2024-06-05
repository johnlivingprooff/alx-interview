#!/usr/bin/node

const rp = require('request-promise-native');

const number = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${number}/`;

// Function to get character data
async function findPerson (url) {
  try {
    const response = await rp(url);
    const data = JSON.parse(response);
    return data.name;
  } catch (error) {
    console.error('Error fetching character data:', error);
    return null;
  }
}

// Function to fetch film data and characters
async function fetchFilmAndCharacters () {
  try {
    const response = await rp(url);
    const data = JSON.parse(response);
    const characters = data.characters;
    const characterPromises = characters.map(findPerson);
    const characterNames = await Promise.all(characterPromises);
    characterNames.forEach(name => {
      if (name) {
        console.log(name);
      }
    });
  } catch (error) {
    console.error('Error fetching film data:', error);
  }
}

// Run the function
fetchFilmAndCharacters();
