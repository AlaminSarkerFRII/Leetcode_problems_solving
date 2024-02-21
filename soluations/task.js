const list = ["song1", "song2", "song3", "song4", "song5"];
let remainingSongs = [...list]; // Create a copy of the original list

function play() {
  if (remainingSongs.length > 0) {

    let randomSong;
    
    if (remainingSongs.length === list.length) {
      randomSong = "song3";
      remainingSongs.splice(remainingSongs.indexOf(randomSong), 1);
    } else {
      const randomIndex = Math.floor(Math.random() * remainingSongs.length);
      randomSong = remainingSongs[randomIndex];
      remainingSongs.splice(randomIndex, 1);
    }

    console.log(randomSong);
  } else {
    console.log("No song left to play");
  }
}

// Example calls to play
play();
play();
play();
play();
play();
play(); // No song left to play
