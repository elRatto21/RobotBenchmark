import open from 'open';
import robot from 'robotjs';

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const screensize = robot.getScreenSize();
const width = screensize.width / 3;
const height = screensize.height / 2;
const GREEN = "4bdb6a";

let tries = 0;

async function start() {
  await open("https://humanbenchmark.com/tests/reactiontime");

  await sleep(3000);

  robot.dragMouse(width, height);
  robot.mouseClick("left");

  while (tries < 5) {
    if (robot.getPixelColor(width, height) === GREEN) {
      robot.mouseClick();
      await sleep(1000);
      robot.mouseClick();
      tries++;
    }
  }
}

start();