$(document).ready(() => {
        // Fetch character name from the provided URL
        $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
          // Update the content of the div with id "character" with the character name
          $('#character').text(data.name);
        });
      });
