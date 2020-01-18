const r = 10;
const maxTries = 30;
const w = r / Math.sqrt(2);
let rows, cols;
let activeList = [];
let grid = [];

function setup() {
  createCanvas(1400, 700);
  background(0);

  rows = floor(height / w);
  cols = floor(width / w);
  // console.log(rows, cols);
  grid = new Array();
  for (let i = 0; i < rows * cols; i++) {
    grid[i] = undefined;
  }
  let x = random(0, width);
  let y = random(0, height);
  let i = floor(x / w);
  let j = floor(y / w);
  let pos = createVector(x, y);
  console.log(pos);
  grid[i + j * cols] = pos;
  activeList.push(pos);
}

function main() {
  for (let i = 0; i < 50; i++) {
    if (activeList.length > 0) {
      let rand = floor(random(activeList.length));
      let pos = activeList[rand];
      let found = false;
      for (let n = 0; n < maxTries; n++) {
        let sample = p5.Vector.random2D();
        let m = random(r, 2 * r);
        sample.setMag(m);
        sample.add(pos);

        let col = floor(sample.x / w);
        let row = floor(sample.y / w);
        if (
          col > -1 &&
          col < cols &&
          row > -1 &&
          row < rows &&
          !grid[col + row * cols]
        ) {
          let active = true;
          for (let i = -1; i <= 1; i++) {
            for (let j = -1; j <= 1; j++) {
              let index = col + i + (row + j) * cols;
              let newSample = grid[index];
              if (newSample) {
                let d = p5.Vector.dist(sample, newSample);
                if (d < r) {
                  active = false;
                }
              }
            }
          }

          if (active) {
            found = true;
            grid[col + row * cols] = sample;
            activeList.push(sample);
            break;
          }
        }
      }

      if (!found) {
        activeList.splice(rand, 1);
      }
    }
  }

  for (let i of grid) {
    if (i) {
      stroke("white");
      circle(i.x, i.y, 2);
    }
  }

  for (let j of activeList) {
    stroke("red");
    circle(j.x, j.y, 2);
  }
}

function draw() {
  background(0);
  // frameRate(60);
  main();
  if (activeList.length === 0) {
    noLoop();
  }
  // console.log(activeList.length);
}
