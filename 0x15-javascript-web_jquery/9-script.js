$(document).ready(() => {

        $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
          // Update the content of the div with id "hello" with the translation
          $('#hello').text(data.hello);
        });
      });
