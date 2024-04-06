
/*
https://stackoverflow.com/questions/39565706/post-request-with-fetch-api

async getData() {
  try {
      let response = await fetch('https://example.com/api');
      let responseJson = await response.json();
      console.log(responseJson);
  } catch(error) {
      console.error(error);
  }
}

fetch("http://example.com/api/endpoint/", {
    method: "post",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },

    //make sure to serialize your JSON body
    body: JSON.stringify({
      name: myName,
      password: myPassword
    })
  })
  .then( (response) => { 
    //do something awesome that makes the world a better place
  });

  fetch("/url-to-post",
  {
      method: "POST",
      // whatever data you want to post with a key-value pair
      body: "name=manas&age=20",
      headers: 
      {
          "Content-Type": "application/x-www-form-urlencoded"
      }
  
  }).then((response) => 
  { 
      // do something awesome that makes the world a better place
  });

const asyncGetCall = async () => {
  try {
      const response = await fetch('https://jsonplaceholder.typicode.com/posts');
       const data = await response.json();
          console.log(data);
     } catch(error) {
  // enter your logic for when there is an error (ex. error toast)
        console.log(error)
       } 
  }


const asyncPostCall = async () => {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
         method: 'POST',
         headers: {
           'Content-Type': 'application/json'
           },
           body: JSON.stringify({
             title: "My post title",
             body: "My post content."
            })
         });
         const data = await response.json();
      // enter you logic when the fetch is successful
         console.log(data);
       } catch(error) {
          console.log(error)
         } 
    }

asyncPostCall()



*/